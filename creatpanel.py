import os, re, time, json, random, string
import requests
from bs4 import BeautifulSoup
from faker import Faker
import textwrap

TOTAL_COOKIES = 0


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://tempmail.lol/",
    "Origin": "https://tempmail.lol",
    "Connection": "keep-alive",
}

# ============================
#  RANDOM TANGGAL LAHIR
# ============================
b_day   = random.randint(1, 28)
b_month = random.randint(1, 12)
b_year  = random.randint(1993, 2007)

r = "\x1b[1;31m"  # merah
g = "\x1b[1;32m"  # hijau
y = "\x1b[1;33m"  # kuning
b = "\x1b[1;34m"  # biru
m = "\x1b[1;35m"  # ungu
c = "\x1b[1;36m"  # cyan
w = "\x1b[1;37m"  # putih
reset = "\x1b[0m" # reset warna
W = "\x1b[97m"
G = "\x1b[38;5;46m"
R = "\x1b[38;5;196m"
X = f"{W}<{R}•{W}>"

LKLK = "male"
pwpw = "rahasia"

faker = Faker()

oks = []
cps = []
    
# =========================
# PANEL SUCCESS
# =========================
def success_panel(data, width=78):
    print(f"{g}SUCCESS{reset}")
    print(f"{g}Akun Berhasil Dibuat - UID {data['uid']}{reset}")

    print(f"{y}┌" + "─" * (width - 2) + f"┐{reset}")
    print(f"{y}│ {g}Informasi Akun Lengkap".ljust(width - 1) + f"{y}│{reset}")

    for k, v in data.items():
        if k == "uid":
            continue
        line = f"{k:<15}: {v}"
        print(f"{y}│ {w}{line.ljust(width - 4)}{y} │{reset}")

    print(f"{y}└" + "─" * (width - 2) + f"┘{reset}")
    
# =========================
#   PREMIUM USER-AGENT
# =========================
def generate_ua():
    android = random.choice(['10','11','12','13','14'])
    build = random.choice(['TP1A','UP1A','RKQ1','SP1A','QP1A'])
    device = random.choice([
        'SM-A546B','SM-S911B','SM-M236B','SM-A037G','SM-A115U','SM-G610M',
        'Infinix X688B','Infinix X689D','Infinix Zero 30','Infinix GT 20 Pro',
        'RMX3630','RMX3686','Realme 12 Pro','Realme GT Neo 5',
        'Xiaomi 13','Xiaomi 13T Pro','22071212AG','Redmi Note 12 Pro',
        'Vivo V27','Vivo Y36','V2242A',
        'OPPO Reno 10','OPPO Find N3','CPH2185'
    ])
    chrome_major = random.randint(110, 128)
    chrome_sub = random.randint(4000, 5900)

    ua = (
        f"Mozilla/5.0 (Linux; Android {android}; {device} Build/{build}.{random.randint(111111,250000)}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_major}.0.{chrome_sub}.{random.randint(40,180)} Mobile Safari/537.36"
    )
    return ua


# =========================
#  HTML INPUT EXTRACTOR
# =========================
def extractor(data):
    soup = BeautifulSoup(data, "html.parser")
    result = {}
    for x in soup.find_all("input"):
        name = x.get("name")
        value = x.get("value")
        if name:
            result[name] = value
    return result

# ====================================================
#  RANDOM GMAIL
# ====================================================
def RandomEmail():
    # Domain random
    domains = [
        "gmail.com",
        "hotmail.com",
        "yahoo.com",
        "outlook.com",
        "mail.com",
        "protonmail.com"
    ]

    first = faker.first_name().lower()
    last  = faker.last_name().lower()
    angka = random.randint(10, 9999)
    domain = random.choice(domains)

    return f"{first}{last}{angka}@{domain}"

# ====================================================
#  GET EMAIL (tempMail.lol)
# ====================================================
def GetEmail():
    try:
        r = ses.get("https://api.tempmail.lol/generate", timeout=10).json()
        return r["address"]
    except Exception as e:
        print("EMAIL ERROR:", e)
        return None


def GetCode(email):
    try:
        url = f"https://api.tempmail.lol/messages?email={email}"

        r = ses.get(url, timeout=10)

        try:
            data = r.json()
        except:
            return None

        if "result" not in data:
            return None

        for msg in data["result"]:
            body = (
                msg.get("body", "") +
                msg.get("text", "") +
                msg.get("html", "")
            )

            m = re.search(r"FB-(\d+)", body)
            if m:
                return m.group(1)

        return None

    except Exception as e:
        print("DEBUG ERROR:", e)
        return None
    
# =========================
#  UI PRINT
# =========================
def banner():
    os.system("clear")
    print(f"{W}<{R}•{W}> FACEBOOK AUTO ID CREATOR")
    print(f"{W}<{R}•{W}> CLEAN VERSION")
    print(f"{W}———————————————————————————————")


def linex():
    print(f"{W}———————————————————————————————")

ses = requests.Session()
ses.headers.update(HEADERS)


# =========================
#  MAIN REG PROCESS
# =========================
def main():
    banner()
    input(f"{X} PRESS ENTER TO START....")
    linex()

    for make in range(700):
        time.sleep(3)
        
        ses = requests.Session()

        # GET FORM
        resp = ses.get("https://x.facebook.com/reg")
        form = extractor(resp.text)

        # EMAIL + NAME
        email = RandomEmail()
        first = faker.first_name()
        last = faker.last_name()

        linex()
        print(f"{X} NAME     : {c}{first} {last}")
        print(f"{X} EMAIL    : {c}{email}")

        # PAYLOAD REGISTRATION
        payload = {
            'ccp': "2",
            'reg_instance': form["reg_instance"],
            'submission_request': "true",
            'reg_impression_id': form["reg_impression_id"],
            'ns': "1",
            'app_id': "103",
            'logger_id': form["logger_id"],

            'field_names[0]': "firstname",
            'firstname': first,
            'lastname': last,

            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(b_day),
            'birthday_month': str(b_month),
            'birthday_year': str(b_year),


            'field_names[2]': "reg_email__",
            'reg_email__': email,

            'field_names[3]': "sex",
            'sex': "2",

            'field_names[4]': "reg_passwd__",
            'encpass': f"#PWD_BROWSER:0:{int(time.time())}:ahmantap1",

            'submit': "Sign Up",

            'fb_dtsg': form.get("fb_dtsg", ""),
            'jazoest': form["jazoest"],
            'lsd': form["lsd"],

            '__dyn': "",
            '__csr': "",
            '__req': "p",
            '__a': "",
            '__user': "0"
        }

        # FIXED HEADERS
        headers = {
            "Host": "m.facebook.com",
            "User-Agent": generate_ua(),
            "Accept": "text/html,application/xhtml+xml",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://m.facebook.com",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Site": "same-origin",
            "Accept-Language": "en-US,en;q=0.9",
        }

        reg_url = "https://www.facebook.com/reg/submit/?multi_step_form=1&shouldForceMTouch=1"
        submit = ses.post(reg_url, data=payload, headers=headers)

        if "c_user" in ses.cookies.get_dict():
            uid = ses.cookies.get_dict()["c_user"]
            print(f"{X} FB UID   : {c}{uid}")

            otp = GetCode(email)
            if otp:
                print(f"{X} EMAIL OTP      - {c}{otp}")
                confirm(uid, email, otp, ses)
            else:                              
                ck = ";".join([f"{k}={v}" for k,v in ses.cookies.get_dict().items()])

                print("\033[F\033[K" * 5, end="")
                data = {
                    "uid": uid,
                    "Nama Lengkap": f"{first} {last}",
                    "Password": pwpw,
                    "Email": email,
                    "Jenis Kelamin": LKLK,
                    "Tanggal Lahir": f"{b_day}/{b_month}/{b_year}",
                    "Total (Run Ini)": TOTAL_COOKIES,
                    "Cookie": ck
                }

                success_panel(data)


                open("/sdcard/CREAT_PARADISE_TIMEOUT.txt","a").write(f"{uid}|ahmantap1|{ck}\n")
                TOTAL_COOKIES += 1
                linex()
                
        else:
            print("\033[F\033[K" * 4, end="")
            print(f"{X} {R}CHECKPOINT")


# =========================
#  CONFIRM ACCOUNT
# =========================
def confirm(uid, mail, otp, ses):
    try:
        params = {
            "contact": mail,
            "type": "submit",
            "medium": "email",
            "code": otp
        }

        payload = {
            "fb_dtsg": "",
            "jazoest": "24384",
            "lsd": "",
            "__dyn": "",
            "__csr": "",
            "__req": "4",
            "__a": "",
            "__user": uid,
        }

        headers = {
            "User-Agent": generate_ua(),
            "Accept": "*/*",
            "Origin": "https://m.facebook.com",
            "X-Requested-With": "XMLHttpRequest"
        }

        res = ses.post("https://m.facebook.com/confirmation_cliff/", params=params, data=payload, headers=headers)

        if "checkpoint" in res.url:
            print(f"{X}{R} DISABLED AFTER OTP")
            linex()
            return

        ck = ";".join([f"{k}={v}" for k,v in ses.cookies.get_dict().items()])
        print(f"{X} OK - {G}{uid}|ahmantap1|{ck}")
        open("/sdcard/CREAT_PARADISE.txt","a").write(f"{uid}|ahmantap1|{ck}\n")
        linex()

    except Exception:
        linex()
        pass


# =========================
#  RUN
# =========================
if __name__ == "__main__":
    main()












