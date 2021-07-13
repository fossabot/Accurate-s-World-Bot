from logging import DEBUG
import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, NoEntryPointError
import json
import sys
from termcolor import colored


client = commands.Bot(command_prefix="!")
DEBUG = colored("DEBUG", "green")
FATAL = colored("FATAL", "red")
WARNING = colored("WARNING", "yellow")
with open("src\SECRET.json", "r")as f:
    settings = json.load(f)
    
    
@client.event
async def on_connect():
    print(f"[{DEBUG}] Successfully connected to Discord Servers")
    
    
@client.event
async def on_disconnect():
    print(f"[{FATAL}] Disconnect from Discord servers. Exiting.")
    sys.exit()


@client.event
async def on_ready():
    print(f"[{DEBUG}] Bot is online")
        
        
@client.command(name="ping", brief="Display Bot ping")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=str(client.latency) + "ms", color=0x3029b3)
    await ctx.channel.send(embed=embed)
    return 0
  
        
try:
    client.load_extension("extensions.leveling")
    
except ExtensionAlreadyLoaded:
    print(f"[{WARNING}] Cog Already loaded.")

except NoEntryPointError:
    raise "[FATAL] Cog does not have a setup function!"

except ExtensionFailed as err:
    with open("DEBUG/TRACE.txt", "w") as f:
        f.append(err)
        
    raise f"[{FATAL}] Extension failed loading (runtime error)! Traceback was stored in DEBUG/TRACE.txt"


client.run(settings["token"])
   
    