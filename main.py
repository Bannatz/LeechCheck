from bs4 import BeautifulSoup as soup
import requests, sys, cloudscraper
import re as reg
from proxychecker import proxycheck
from utils import cprint, savename, log, delDup
"""
1. Abfrage wie viele Seiten er scrapen soll
2. die in einen Array packen damit wir einen For Loop für Requests machen können.
3. die page mit einem HTML Parser absuchen nach dem Tag "a" und der Klasse "link"
4. For loop für jeden href er findet einen request senden und den parsen nach "h6"/Paste Name
5. For loop nach der "textarea"/Alles was in dem Paste drinne steht
6. Öffne eine Datei schreibe die URL die gerade gelesen wird rein und den Inhalt der Seite
"""
def proxy():
    cprint("[LC] Do you want to check the proxies?[y/N] ", "green")
    ans = input("")
    if ans == "Y" or ans == "y":
        cprint("[LC] How many threads? ", "green")
        try:
            threads = int(input(""))
        except Exception:
            print("stopllolol")
            threads = 1
        with open(savename("proxies", "txt", -1), "r") as f:
            plist = f.readlines()
            f.close()
        
        p = proxycheck(proxy_list=plist, threads=threads)
        p.init_check()

    else:
        pass

def main():
    scraper = cloudscraper.create_scraper()
    s = int(input("How many sites (2 for one Site): "))
    log(init=True)
    string = "/"
    combos = []
    usercombos = []
    proxys = []
    for i in range(1, s):
        urls = []
        pagelist = f"https://pastehub.net/recent.php?p={i}"
        urls.append(pagelist) 
        for url in urls: # for loop für die URLs
            cprint(f"{url}\n\n", "blue")
            page = scraper.get(url)
            jesus = soup(page.content, 'html.parser')
            for i in jesus.find_all('a', class_="link", href=True):
                re = scraper.get("https://pastehub.net/" + i.text)
                jesus3 = soup(re.content, "html.parser")
                pagename = jesus3.find('h6')
                cprint(pagename.text + " | " + "https://pastehub.net/" + i.text + "\n", "green")
                pagename = pagename.text.replace(string, "")
                for f in jesus3.find_all('textarea'):
                    check = reg.findall(r".{1,}[@].{1,}\.[a-z]{1,}[:].{1,}", str(f.text))
                    log(f"[URL: {url}]\n{check}")
                    pcheck = reg.findall(r"[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,4}", str(f.text))
                    log(pcheck)
                    ucheck = reg.findall(r"([a-zA-Z0-9.]{1,})(?<!com):([a-zA-Z0-9]{1,}.[a-zA-Z0-9]{1,})", str(f.text)) # [a-zA-Z0-9] a-z groß und klein {1,} einmal bis unendlich [:] Doppelpunkt, . für jeden Character(!,\,$), {1,} eins bis ins unendliche
                    log(ucheck)
                    cprint(f"Combos: {len(check)}\n", "green")
                    cprint(f"User:Pass Combos: {len(ucheck)}\n", "green")
                    cprint(f"Proxies: {len(pcheck)}\n\n", "green")
                    cz = len(check)
                    pz = len(pcheck)
                    uz = len(ucheck)
                    z = 0
                    for combo in check:
                        temp = str(combo).split(" ")
                        combo = temp[0]
                        sys.stdout.write(f"Appending Combo: {combo}\r")
                        sys.stdout.write("\033[K")
                        combos.append(str(combo))
                    for proxy in pcheck:
                        temp = str(proxy).split(" ")
                        sys.stdout.write(f"Appending Proxy: {proxy}\r")
                        sys.stdout.write("\033[K")
                        proxys.append(str(proxy))
                        z += 1
                        if z == pz:
                            break
                    for ucombo in ucheck:
                        ucombo[1] = ucombo[1].trim()
                        sys.stdout.write(f"Appending Proxy: {ucombo}\r")
                        sys.stdout.write("\033[K")
                        userpass = ucombo[0] + ":" + ucombo[1]
                        usercombos.append(userpass)
                        z += 1
                        if z == pz:
                            break

    with open(savename("combos", "txt"), "a") as k:
        for combo in delDup(combos):
            combo = str(combo).replace("\r", "")
            k.write(f"{combo}\n") 
        k.close()
    with open(savename("proxies", "txt"), "a") as k:
        for proxy in delDup(proxys):
            proxy = str(proxy).replace("\r", "")
            k.write(f"{proxy}\n")
        k.close()
    with open(savename("userpass", "txt"), "a") as k:
        for userpw in delDup(usercombos):
            userpw = str(userpw).replace("\r", "")
            k.write(f"{userpw}\n")


def search():
    keyword = str(input("Enter Keyword(example: Minecraft Combos): "))    
    scraper = cloudscraper.create_scraper()
    i = 0
    urls = []
    combos = []
    ucombos = []
    proxies = []
    if keyword == "":
        print("Please specify a keyword!")
        keyword = str(input("Enter Keyword: "))
    elif " " in keyword:
        keyword.replace(" ", "+")
    elif "proxy" or "Proxy" in keyword:
        page = scraper.get("https://searchresults.cc/" + keyword)
        jesus = soup(page.content, 'html.parser')
        for i in jesus.find_all("a", href=True):
            if i.text.startswith("https://pastehub.net") == True:
                urls.append(i.text)
        for url in urls:
            page = scraper.get(url)
            jesus = soup(page.content, 'html.parser')
            cprint(f"{url}\n\n", "blue")
            pagename = jesus.find("h6")
            for f in jesus.find_all('textarea'):
                check = reg.findall(r"[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,4}", str(f.text))
                for proxy in check:
                    temp = str(proxy).split(" ")
                    sys.stdout.write(f"Appending Proxies: {proxy}\r")
                    sys.stdout.write("\033[K")
                    proxies.append(str(proxy))
        with open(savename(f"{keyword}", "txt"), "a") as f:
            for proxy in delDup(proxies):
                proxy = str(proxy).replace("\r", "")
                f.write(f"{proxy}\n")
            f.close()
    page = scraper.get("https://searchresults.cc/" + keyword)
    jesus = soup(page.content, 'html.parser')
    for i in jesus.find_all("a", href=True):
        if i.text.startswith("https://pastehub.net") == True:
            urls.append(i.text)
    for url in urls:
        page = scraper.get(url)
        jesus = soup(page.content, 'html.parser')
        cprint(f"{url}\n\n", "blue")
        pagename = jesus.find("h6")
        for f in jesus.find_all('textarea'):
            check = reg.findall(r".{1,}[@].{1,}\.[a-z]{1,}[:].{1,}", str(f.text))
            ucheck = reg.findall(r"([a-zA-Z0-9.]{1,})(?<!com):([a-zA-Z0-9]{1,}.[a-zA-Z0-9]{1,})", str(f.text))
        for upass in ucheck:
            userpasscmb = upass[0] + ":" + upass[1]+ "\n"
            sys.stdout.write(f"Appending User:Pass Combo: {upass}\r")
            sys.stdout.write("\033[K")
            ucombos.append(str(userpasscmb))
        for combo in check:
                temp = str(combo).split(" ")
                combo = temp[0]
                sys.stdout.write(f"Appending Combo: {combo}\r")
                sys.stdout.write("\033[K")
                combos.append(str(combo))
    with open(savename(f"{keyword}", "txt"), "a") as f:
        for combo in delDup(combos):
            combo = str(combo).replace("\r", "")
            f.write(f"{combo}\n")
        if ucombos != None:
            with open(savename(f"UserPass_{keyword}", "txt"), "a") as k:
                for upass in delDup(ucombos):
                    upass = str(upass).replace("\r", "")
                    k.write(upass)
        f.close()
    
def menu():
    cprint("""

.____                        .__    _________ .__                   __                
|    |    ____   ____   ____ |  |__ \_   ___ \|  |__   ____   ____ |  | __            
|    |  _/ __ \_/ __ \_/ ___\|  |  \/    \  \/|  |  \_/ __ \_/ ___\|  |/ /            
|    |__\  ___/\  ___/\  \___|   Y  \     \___|   Y  \  ___/\  \___|    <             
|_______ \___  >\___  >\___  >___|  /\______  /___|  /\___  >\___  >__|_ \            
        \/   \/     \/     \/     \/        \/     \/     \/     \/     \/            
__________                  __           ___ ___      ___.                       __   
\______   \_____    _______/  |_  ____  /   |   \ __ _\_ |__        ____   _____/  |_ 
 |     ___/\__  \  /  ___/\   __\/ __ \/    ~    \  |  \ __ \      /    \_/ __ \   __\
 |    |     / __ \_\___ \  |  | \  ___/\    Y    /  |  / \_\ \    |   |  \  ___/|  |  
 |____|    (____  /____  > |__|  \___  >\___|_  /|____/|___  / /\ |___|  /\___  >__|  
                \/     \/            \/       \/           \/  \/      \/     \/      

""", 'green')
    print("Welcome to LeechCheck!\n[1] Leech Recent Combos\n[2] Search Combos for Specific Keyword")
    s = int(input("> "))
    if s == 1:
        main()
    elif s == 2:
        search()
    else:
        pass
menu()
proxy()
