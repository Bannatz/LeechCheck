from bs4 import BeautifulSoup as soup
import cloudscraper
import re as reg
from proxychecker import proxycheck
from os import mkdir, path
from utils import cprint, listToFile, saveName, delDup


def proxy():
    cprint("[LC] Do you want to check the proxies?[y/N] ", "green")
    ans = input("")
    if ans == "Y" or ans == "y":
        cprint("[LC] How many threads? ", "green")
        try:
            threads = int(input(""))
        except Exception:
            threads = 1
        with open(saveName("proxies/proxies", "txt", -1), "r") as f:
            plist = f.readlines()
        
        p = proxycheck(proxy_list=plist, threads=threads)
        p.init_check()
    else:
        pass

def main():
    try:
        s = int(input("How many sites: ")) + 1
    except Exception:
        exit()

    if(s < 1):
        s = 1

    check = []
    pcheck = []

    urls = [f"https://pastehub.net/recent.php?p={i}" for i in range(1, s)]

    scraper = cloudscraper.create_scraper()
    for url in urls: # for loop für die URLs
        cprint(f"{url}\n", "green")
        page = scraper.get(url)
        jesus = soup(page.content, 'html.parser')

        for i in jesus.find_all('a', class_="link", href=True):
            re = scraper.get(f"https://pastehub.net/{i.text}")
            jesus3 = soup(re.content, "html.parser")

            for f in jesus3.find_all('textarea'):
                check.extend(reg.findall(r".{1,}[@].{1,}\.[a-z]{1,}[:].{1,}", str(f.text)))
                pcheck.extend(reg.findall(r"[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,4}", str(f.text)))

    combos = delDup([str(combo).split(" ")[0].replace("\r", "") for combo in check])

    proxies = delDup([str(proxy).split(" ")[0].replace("\r", "") for proxy in pcheck])

    listToFile("combos/combos", combos)

    listToFile("proxies/proxies", proxies)

    print(f"\n>> Finished <<\nCombos: {len(combos)}\nProxies: {len(proxies)}\n")


def search():
    keyword = input("Enter Keyword(example: Minecraft Combos): ").lower().replace(" ", "+").strip()
    if keyword == "":
        exit()
    scraper = cloudscraper.create_scraper()
    check = []
    check_proxies = False

    if "proxy" or "proxies" in keyword:
        check_proxies = True

        page = scraper.get(f"https://searchresults.cc/{keyword}")
        urls = [link.text for link in soup(page.content, 'html.parser').find_all("a", href=True) if link.text.startswith("https://pastehub.net")]
        for url in urls:
            cprint(f"{url}\n\n", "blue")
            page = scraper.get(url)
            for f in soup(page.content, 'html.parser').find_all('textarea'):
                if(check_proxies):
                    check.extend(reg.findall(r"[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,4}", str(f.text)))
                else:
                    check.extend(reg.findall(r".{1,}[@].{1,}\.[a-z]{1,}[:].{1,}", str(f.text)))
                
        
        check = delDup([str(x).split(" ")[0].replace("\r", "") for x in check])

        listToFile(f"keyword/{keyword}", check)
    
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

if __name__ == "__main__":
    if(path.isdir("./combos") is False): 
        mkdir("./combos")
    
    if(path.isdir("./proxies") is False):
        mkdir("./proxies")
    
    if(path.isdir("./keyword") is False):
        mkdir("./keyword")

    menu()
    proxy()
