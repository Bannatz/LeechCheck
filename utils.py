from os import path
from sys import stdout

def delDup(alist: list):
    new = list(dict.fromkeys(alist))
    return new

def listRemoveNewLines(alist: list):
    new = [str(x).replace("\n", "") for x in alist]
    return new

def saveName(file: str, suffix: str, shift: int = 0):
    i = 1
    while path.isfile(f"{file}{i}.{suffix}"):
        i += 1
    
    return f"{file}{i+shift}.{suffix}"

def listToFile(save_path: str, alist: list):
    with open(saveName(save_path, "txt"), "a") as k:
        for item in alist:
            k.write(f"{item}\n")

def log(input: any = "", init: bool = False):
    if init:
        with open("debug.log", mode="w", encoding="utf-8") as f:
            f.write("")
    else:
        with open("debug.log", mode="a", encoding="utf-8") as f:
            f.write(f"{str(input)}\n\n")

def cprint(text: str, color: str, bg_color: str = None, format: str = None):
    formats = {
    'bold' : '\033[01m',
    'disable' : '\033[02m',
    'underline' : '\033[04m',
    'reverse' : '\033[07m',
    'strikethrough' : '\033[09m',
    'invisible' : '\033[08m',
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
    'black' : '\033[40m',
    'red' : '\033[41m',
    'green' : '\033[42m',
    'orange' : '\033[43m',
    'blue' : '\033[44m',
    'purple' : '\033[45m',
    'cyan' : '\033[46m',
    'lightgrey' : '\033[47m'
    }

    ocolor = ""
    oform = ""
    obg = ""

    # color
    try:
        if color is not None:
            ocolor = colors.get(color)
    except Exception:
        pass

    # background color
    try:
        if bg_color is not None:
            obg = bgcolors.get(bgcolors)
    except Exception:
        pass

    #format
    try:
        if format is not None:
            oform = formats.get(format)
    except Exception:
        pass

    stdout.write(f"{obg}{ocolor}{oform}{text}\033[0m")
    stdout.flush()