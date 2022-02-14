from lxml import html
from bs4 import BeautifulSoup as soup
import requests, os, sys, art
import re as reg
from utils import cprint, savename, log
"""
1. Abfrage wie viele Seiten er scrapen soll
2. die in einen Array packen damit wir einen For Loop für Requests machen können.
3. die page mit einem HTML Parser absuchen nach dem Tag "a" und der Klasse "link"
4. For loop für jeden href er findet einen request senden und den parsen nach "h6"/Paste Name
5. For loop nach der "textarea"/Alles was in dem Paste drinne steht
6. Öffne eine Datei schreibe die URL die gerade gelesen wird rein und den Inhalt der Seite!
"""

def delDup(clist: list):
    clist = list(dict.fromkeys(clist))
    return clist
        

""" def savename(file: str):
    i = 1
    if file == "combo":
        while os.path.isfile(f"Combos{i}.txt"):
            i += 1
        return f"Combos{i}.txt"
    elif file == "proxy":
        while os.path.isfile(f"Proxies{i}.txt"):
            i += 1
        return f"Proxies{i}.txt"
    elif file == "userpass":
        while os.path.isfile(f"User_Pass Combos{i}.txt"):
            i += 1
        return f"User_Pass Combos{i}.txt" """
        
def main():
    cprint("""

  /$$$$$$  /$$$$$$  /$$$$$$          /$$                                     /$$                                
 /$$__  $$|_  $$_/ /$$__  $$        | $$                                    | $$                                
| $$  \ $$  | $$  | $$  \ $$        | $$        /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$       
| $$$$$$$$  | $$  | $$  | $$ /$$$$$$| $$       /$$__  $$ /$$__  $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$      
| $$__  $$  | $$  | $$  | $$|______/| $$      | $$$$$$$$| $$$$$$$$| $$      | $$  \ $$| $$$$$$$$| $$  \__/      
| $$  | $$  | $$  | $$  | $$        | $$      | $$_____/| $$_____/| $$      | $$  | $$| $$_____/| $$            
| $$  | $$ /$$$$$$|  $$$$$$/        | $$$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$| $$            
|__/  |__/|______/ \______/         |________/ \_______/ \_______/ \_______/|__/  |__/ \_______/|__/            
                                                                                                                
                                                                                                                
                                                                                                                
 /$$$$$$$                       /$$               /$$                 /$$                                /$$    
| $$__  $$                     | $$              | $$                | $$                               | $$    
| $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$$$$$$  /$$   /$$| $$$$$$$     /$$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$$$/|____  $$ /$$_____/|_  $$_/   /$$__  $$| $$__  $$| $$  | $$| $$__  $$   | $$__  $$ /$$__  $$|_  $$_/  
| $$____/  /$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$   | $$  \ $$| $$$$$$$$  | $$    
| $$      /$$__  $$ \____  $$  | $$ /$$| $$_____/| $$  | $$| $$  | $$| $$  | $$   | $$  | $$| $$_____/  | $$ /$$
| $$     |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$/| $$$$$$$//$$| $$  | $$|  $$$$$$$  |  $$$$/
|__/      \_______/|_______/    \___/   \_______/|__/  |__/ \______/ |_______/|__/|__/  |__/ \_______/   \___/  
                                                                                                                
                                                                                                                

""", "green")
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
            cprint(f"{url}\n\n", "blue", "black")
            page = requests.get(url)
            jesus = soup(page.content, 'html.parser')
            for i in jesus.find_all('a', class_="link", href=True):
                re = requests.get("https://pastehub.net/" + i.text)
                jesus3 = soup(re.content, "html.parser")
                pagename = jesus3.find('h6')
                cprint(pagename.text + " | " + "https://pastehub.net/" + i.text + "\n", "green")
                pagename = pagename.text.replace(string, "")
                for f in jesus3.find_all('textarea'): 
                    check = reg.findall(r".{1,}[@].{1,}\.[a-z]{1,}[:].{1,}", str(f.text))
                    log(f"[URL: {url}]\n{check}")
                    pcheck = reg.findall(r"[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,4}", str(f.text))
                    log(pcheck)
                    ucheck = reg.findall(r"^[a-zA-Z0-9](_(?!(\.|_))|\.(?!(_|\.))|[a-zA-Z0-9:]){1,}[a-zA-Z0-9]:.{1,}$", str(f.text)) # [a-zA-Z0-9] a-z groß und klein {1,} einmal bis unendlich [:] Doppelpunkt, . für jeden Character(!,\,$), {1,} eins bis ins unendliche
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
                        temp = str(ucombo).split(" ")
                        sys.stdout.write(f"Appending Proxy: {ucombo}\r")
                        sys.stdout.write("\033[K")
                        usercombos.append(ucombo)
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
main()