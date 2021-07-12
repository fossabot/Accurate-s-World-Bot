import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, NoEntryPointError
import json


client = commands.Bot(command_prefix="!")
with open("src\SECRET.json", "r")as f:
    settings = json.load(f)


@client.event
async def on_ready():
    print("Bot is online")
        
        
@client.command(name="ping", brief="Display Bot ping")
async def ping(ctx, *args, **kwargs):
    """Returns Bot Ping

    Args:
        ctx (any): context

    Returns:
        integer: Exit code
    """
    embed = discord.Embed(title="Pong!", description=client.latency + "ms")
    await ctx.channel.send(embed=embed)
    return 0
        
        
try:
    #  client.load_extension("src/extensions/leveling.py")
    client.load_extension("extensions.chat.chatFilter")
    
except ExtensionAlreadyLoaded:
    print("[WARN] Cog Already loaded.")

except NoEntryPointError:
    raise "[FATAL] Cog does not have a setup function!"

except ExtensionFailed as err:
    with open("DEBUG/TRACE.txt", "w") as f:
        f.append(err)
        
    raise "[FATAL] Extension failed loading (runtime error)! Traceback was stored in DEBUG/TRACE.txt"


client.run(settings["token"])
