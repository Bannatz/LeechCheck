import requests, os, sys
from utils import cprint, listRemoveNewLines, listToFile, saveName
from concurrent.futures import ThreadPoolExecutor

class proxycheck:
    def __init__(self, proxy_list: list, threads: int) -> None:
        self.plist = listRemoveNewLines(proxy_list)
        self.threads = threads
        self.working = []
        self.len = len(self.plist)
        self.counter = 1
        
    def save_working(self):
        if os.path.isdir("checked_proxies") is False:
            os.mkdir("checked_proxies")
        listToFile("checked_proxies/checked_proxies", self.working)

    def proxy_check(self, proxy: str):
        try:
            try:
                res = requests.get(url="https://example.com", proxies={"https" : proxy}, timeout=10)
                res.close()
                self.working.append(proxy)
            except Exception:
                pass

            self.counter += 1
            sys.stdout.write("\033[K")
            cprint(f" {proxy}\t[{self.counter}/{self.len}]\t{len(self.working)} working\r", "green")
        except KeyboardInterrupt:
            self.save_working()
            exit()

    def init_check(self):
        with ThreadPoolExecutor(self.threads) as x:
            x.map(self.proxy_check,self.plist)

        self.save_working()