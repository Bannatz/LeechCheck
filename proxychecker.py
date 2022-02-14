import requests, os, sys
from utils import cprint, listRemoveNewLines, log, savename

def save_working(working: list):
    if os.path.isdir("proxies") is False:
        os.mkdir("proxies")
    with open(savename("proxies/working", "txt"), "a") as f:
        for proxy in working:
            f.write(f"{proxy}\n")
        f.close()

def proxy_check(proxy_list: list):
    proxy_list = listRemoveNewLines(proxy_list)
    working = []

    l = len(proxy_list)
    z = 1

    for proxy in proxy_list:
        sys.stdout.write("\033[K")
        cprint(f" Testing: {proxy}\t[{z}/{l}]\r", "green")
        z += 1
        p = {"https": proxy}
        try:
            r = requests.get(url="https://example.com", proxies=p, timeout=5)
            log(f"[WORKING] {proxy}")
            r.close()
            working.append(proxy)
        except Exception:
            log(f"[NOT WORKING] {proxy}")
    
    save_working(working)