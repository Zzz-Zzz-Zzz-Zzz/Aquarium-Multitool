from time import sleep
from colner import Guild, Restart, Copy
import os
try:
    import discord, asyncio, json, sys, ctypes, time, logging
    from discord.ext import commands
    from os import system
except ImportError:
    os._exit()


logging.basicConfig(level=logging.CRITICAL,format="\x1b[38;5;83m[\033[1;30;48m%(asctime)s\x1b[38;5;83m]\x1b[0m %(message)s\x1b[0m",datefmt="%H:%M:%S")
class misc:
    def clear():
         return system("cls & mode 95,30")

    def title():
        return ctypes.windll.kernel32.SetConsoleTitleW("Glk-Cloner V2")
    clear()
    def load(text):
        try:
          for sex in text:
            print('' + sex, end="")
            sys.stdout.flush()
            time.sleep(0.0200)
        except:
          pass

    ctypes.windll.kernel32.SetConsoleTitleW("Discord-Cloner V2 - Loading")
    load(r"""
         
               ____  ____    ____  _     ____  _      _____ ____  
               /  _ \/   _\  /   _\/ \   /  _ \/ \  /|/  __//  __\ 
               | | \||  /    |  /  | |   | / \|| |\ |||  \  |  \/| 
               | |_/||  \__  |  \__| |_/\| \_/|| | \|||  /_ |    / 
               \____/\____/  \____/\____/\____/\_/  \|\____|\_/\_\ 
            
                                    Loading...
                  
                  
                                                        
    """)



token = input(f'\033[1;35;48mIntroduce tu Token\u001b[0m: \n >')
token = token
commands = {
    
    "copy": {
        ".copy -settings",
        ".copy -roles",
        ".copy -emojis",
        ".copy -channels",
        ".copy -all",
    },

    "exit": {
        ".exit"
    }
}


def main():
    stats = True  # to not error if use exit() method
    while stats:

        command = input("\033[35mElige los comandos para intruducir:\u001b[0m  \033[0m.help/.copy/.exit\033[0m > ")

        if command.startswith(".exit"):  # to exit from tool

            stats = False  # to not get error from stop wihle loop
            exit(-1)

        # to get all commands and author creator
        elif command.startswith(".help"):

            print("C: /discord/gg/glk")
            z = ""
            for com, d in commands.items():  # make help command
                z += com + "\n"
                for i in d:
                    z += "  " + i + "\n"
            print(z)

            command = input("\033[35mIntroduce el comando:\u001b[0m  \033[0m.copy [choice]\033[0m > ")

            if command.startswith(".exit"):  # to exit from tool

             stats = False  # to not get error from stop wihle loop
             exit(-1)

        # to restart all objects from guild example: roles, channels, emojis, ...
        elif command.startswith(".restart"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue
            print("restart roles...")
            restart = Restart(guild)
            restart.roles()

        # copy roles and add to cache memory if you need copy the server tow in run one you have get error

        elif command.startswith(".copy -channels") or command.startswith(".copy -c"):
            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)
            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.copy_channels()

        elif command.startswith(".copy -roles") or command.startswith(".copy -r"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)
            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.create_roles()

        # just copy emojis
        elif command.startswith(".copy -emojis") or command.startswith(".copy -e"):
            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.create_emojis()

        # to copy: icon, name, description, ...
        elif command.startswith(".copy -settings") or command.startswith(".copy -s"):
            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)

            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild()
            if Guild(to_guild_id).get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            copy.update_settings_from_server()

        # this is a great command to copy all roles, channels, emojis, settings
        # the cache imprtant here because synchronization channel permissions with roles 
        elif command.startswith(".copy -all") or command.startswith(".copy -a"):

            guild_id = input("Give me server id: ")
            guild = Guild(guild_id, token)
            if guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            to_guild_id = input("Give me your server id: ")
            to_guild = Guild(to_guild_id, token)
            if to_guild.get_info.get("code"):
                print("\033[91mInvalid server id\033[0m")
                continue

            copy = Copy(guild=guild, to_guild=to_guild)
            restart = Restart(guild=to_guild)

            print("restart roles...")
            restart.roles()
            print("restart channels...")
            restart.channels()
            print("restart roles...")
            restart.roles()
            print("restart emojis...")
            restart.emojis()
            print("copy channels...")
            copy.copy_channels()
            print("copy roles...")
            copy.create_roles()
            print("copy channels...")
            copy.create_channels()
            print("copy emojis...")
            copy.create_emojis()
            print("copy server settings...")
            copy.update_settings_from_server()

if __name__ == "__main__":
    main()