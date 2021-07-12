import discord
from discord.ext import commands
from discord.ext.errors import ExtensionAlreadyLoaded, NoEntryPointError, ExtensionFailed
import json


client = commands.Bot(command_prefix="!")
with open("src\SECRET.json", "r")as f:
    settings = json.load(f)


@client.event
async def on_ready():
    print("Bot is online")
        
        
@client.command(name="ping", brief="Display Bot ping")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=str(client.latency) + "ms", color=0x3029b3)
    await ctx.channel.send(embed=embed)
    return 0
        

client.run(settings["token"])
   
        
try:
    client.load_extension("extensions.leveling")
    
except ExtensionAlreadyLoaded:
    print("[WARN] Cog Already loaded.")

except NoEntryPointError:
    raise "[FATAL] Cog does not have a setup function!"

except ExtensionFailed as err:
    with open("DEBUG/TRACE.txt", "w") as f:
        f.append(err)
        
    raise "[FATAL] Extension failed loading (runtime error)! Traceback was stored in DEBUG/TRACE.txt"

