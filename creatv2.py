import os, re, time, json, random, string
import requests
from bs4 import BeautifulSoup
from faker import Faker

W = "\x1b[97m"
G = "\x1b[38;5;46m"
R = "\x1b[38;5;196m"
m = "\x1b[1;35m"  # ungu
X = f"{W}<{R}•{W}>"

faker = Faker()

oks = []
cps = []


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
#  GET EMAIL (tempMail.lol)
# ====================================================
def GetEmail():
    try:
        r = requests.get("https://api.tempmail.lol/generate").json()
        return r["address"]     # hasil email
    except:
        return None


# ====================================================
#  GET OTP CODE from inbox (tempMail.lol)
# ====================================================
def GetCode(email):
    try:
        inbox = email.replace("@", "%40")
        url = f"https://api.tempmail.lol/messages?inbox={inbox}"

        r = requests.get(url)

        # Jika bukan JSON (403, HTML, dll.)
        try:
            data = r.json()
        except:
            print(f"{r}DEBUG NON-JSON:", r.text[:200])
            return None

        # Struktur valid?
        if not data or "messages" not in data:
            return None

        # Loop semua pesan dalam inbox
        for msg in data["messages"]:
            body = (
                msg.get("body", "") +
                msg.get("text", "") +
                msg.get("html", "")
            )

            match = re.search(r"FB-(\d+)", body)
            if match:
                return match.group(1)

        return None

    except Exception as e:
        print("DEBUG ERROR", e)
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


# =========================
#  MAIN REG PROCESS
# =========================
def main():
    banner()
    input(f"{X} PRESS ENTER TO START....")
    linex()

    for make in range(100):
        ses = requests.Session()

        # GET FORM
        resp = ses.get("https://x.facebook.com/reg")
        form = extractor(resp.text)

        # EMAIL + NAME
        email = GetEmail()
        first = faker.first_name()
        last = faker.last_name()

        print(f"{X} NAME  - {G}{first} {last}")
        print(f"{X} EMAIL - {G}{email}")

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
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1993, 2007)),

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
            print(f"{X} FB UID - {G}{uid}")

            # ===============================
            #   WAIT OTP 5 DETIK
            # ===============================

            print(f"{X} WAITING OTP 20s ...")
            start = time.time()
            otp = None

            while time.time() - start < 20:
                otp = GetCode(email)
                if otp:
                    break
                time.sleep(5)   # cek tiap 5 detik (lebih aman)


            if otp:
                print(f"{X} EMAIL OTP - {G}{otp}")
                confirm(uid, email, otp, ses)
            else:
                ck = ";".join([f"{k}={v}" for k,v in ses.cookies.get_dict().items()])
                print(f"{X} {R}NO OTP RECEIVED (TIMEOUT 20s)")
                open("/sdcard/CREAT_PARADISE_FAILED.txt","a").write(f"{uid}|ahmantap1|{ck}\n")
                linex()

                
        else:
            print(f"{X} {R}CHECKPOINT")
            open("/sdcard/CREAT_PARADISE_CHECKPOINT.txt","a").write(f"{uid}|ahmantap1\n")
            linex()


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


