from datetime import datetime
import json
import time
import os
import sys
import ctypes

name = "Serenitty"
version = "1.0.0"
ci = "‎ "
separ = "――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
aplphabet = "abcdefghijklmnopqrstuvwxyz"
DISCORD_GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json"

RESET = "\033[0m"
GREY = ""
W = "\033[37m"
M = "\033[35m"
G = "\033[32m"
R = "\033[31m"
B = "\033[34m"
O = "\033[33m"

def center(var: str, space: int = None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

banner = f"""
 _____                 _ _   _       
|   __|___ ___ ___ ___|_| |_| |_ _ _ 
|__   | -_|  _| -_|   | |  _|  _| | |
|_____|___|_| |___|_|_|_|_| |_| |_  |
                                |___|
"""
sign = "[!] Dev by Lag3n\n"

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

config = load_json("config.json")
private_config = load_json("config-private.json")
color = config.get('color')
bot_prefix = config.get('prefix')

def Clear():
    os.system('cls' if os.name=='nt' else 'clear')

def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name} v{version} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name} v{version} | {title}\x07")

def Ask(text):
    rep = input(f"{co()}{text}{W} > ")
    return rep

def get_state(state):
    if state == "connect":
        return f"{W}STATUS: {G}CONNECTED{W}"
    elif state == "disconnect":
        return f"{W}STATUS: {R}DISCONNECTED{W}"
    elif state == "connecting":
        return f"{W}STATUS: {RESET}CONNECTING...{W}"

def Menu(state, acc="???", prefix="?"):
    print(co() + center(banner) + RESET)
    print(center(sign))
    print()
    lines = [state]
    if acc: lines.append(f"ACCOUNT: {acc}")
    if prefix: lines.append(f"PREFIX: {prefix}")
    line = ""
    for linee in lines:
        line += linee
        if linee != lines[-1]:
            line += "   |   "
    print(center(line))
    print(center(separ))



def co():
    global color
    return color

def set_color(n_color):
    global color
    color = n_color
    conf = load_json("config.json")
    conf['color'] = color
    save_json("config.json", conf)

def prefix():
    global bot_prefix
    return bot_prefix

def set_prefix(n_prefix):
    global bot_prefix
    bot_prefix = n_prefix
    conf = load_json("config.json")
    conf['prefix'] = bot_prefix
    save_json("config.json", conf)