import requests, os, sys, time
from utils import cprint, listRemoveNewLines, log, savename
from concurrent.futures import ThreadPoolExecutor

class proxycheck:

    def __init__(self, proxy_list: list, threads: int) -> None:
        self.plist = listRemoveNewLines(proxy_list)
        self.threads = threads
        self.working = []
        self.len = len(self.plist)
        self.counter = 1
        
    def save_working(self):
        if os.path.isdir("proxies") is False:
            os.mkdir("proxies")
        with open(savename("proxies/working", "txt"), "a") as f:
            for proxy in self.working:
                f.write(f"{proxy}\n")
            f.close()

    def proxy_check(self, proxy: str):
        p = {"https" : proxy}
        try:
            r = requests.get(url="https://example.com", proxies=p, timeout=10)
            log(f"[WORKING] {proxy}")
            r.close()
            self.working.append(proxy)
        except Exception:
            log(f"[NOT WORKING] {proxy}")

        self.counter += 1 
        cprint(f" {proxy}\t[{self.counter}/{self.len}]\r", "green")
        sys.stdout.write("\033[K")

    def init_check(self):
        log(f"plist: \n{self.plist}\n---------")
        log(f"Threads {self.threads}")
        with ThreadPoolExecutor(self.threads) as x:
            x.map(self.proxy_check,self.plist)

        self.save_working()