import sys, os

def delDup(clist: list):
    clist = list(dict.fromkeys(clist))
    return clist

def listRemoveNewLines(list: list[str]):
    new = []
    for stuff in list:
        stuff = stuff.replace("\n", "")
        new.append(stuff)

    return new

def savename(file: str, suffix: str, shift: int = 0):
    i = 1
    while os.path.isfile(f"{file}{i}.{suffix}"):
        i += 1
    
    return f"{file}{i+shift}.{suffix}"

def log(output: any = "", init: bool = False):
    if init == True:
        with open("debug.log", mode="w", encoding="utf-8") as f:
            f.write("")
            f.close()
    else:
        with open("debug.log", mode="a", encoding="utf-8") as f:
            f.write(f"{str(output)}\n\n")
            f.close()

def cprint(text: str, color: str, bg_color: str = None, pre: str = None, post: str = None):
    pres = {
    'bold' : '\033[01m',
    'disable' : '\033[02m',
    'underline' : '\033[04m',
    'reverse' : '\033[07m',
    'strikethrough' : '\033[09m',
    'invisible' : '\033[08m',
    }

    posts = {
    'reset' : '\033[0m',
    }

    colors = {
    'black' : '\033[30m',
    'red' : '\033[31m',
    'green' : '\033[32m',
    'orange' : '\033[33m',
    'blue' : '\033[34m',
    'purple' : '\033[35m',
    'cyan' : '\033[36m',
    'lightgrey' : '\033[37m',
    'darkgrey' : '\033[90m',
    'lightred' : '\033[91m',
    'lightgreen' : '\033[92m',
    'yellow' : '\033[93m',
    'lightblue' : '\033[94m',
    'pink' : '\033[95m',
    'lightcyan' : '\033[96m'
    }

    bgcolors = {
    'bg_black' : '\033[40m',
    'bg_red' : '\033[41m',
    'bg_green' : '\033[42m',
    'bg_orange' : '\033[43m',
    'bg_blue' : '\033[44m',
    'bg_purple' : '\033[45m',
    'bg_cyan' : '\033[46m',
    'bg_lightgrey' : '\033[47m'
    }

    try:
        out = ""
        if bg_color != None:
            out += bgcolors.get(f"bg_{bg_color}")
    except Exception:
        sys.stdout.write(f"cprint: {bg_color} is not a valid background color!\n")
        sys.exit()
    
    try:
        if pre != None:
            out += pres.get(pre)
    except Exception:
        sys.stdout.write(f"cprint: {pre} is no valid pre\n")
        sys.exit()

    try:
        out += colors.get(color) + text

        try:
            if post != None:
                out += posts.get(post)
        except Exception:
            sys.stdout.write(f"cprint: {post} is no valid post\n")
            sys.exit()

        out += posts.get("reset")
        sys.stdout.write(out)
    except Exception:
        sys.stdout.write(f"cprint: {color} is no valid color!")
        sys.exit()
