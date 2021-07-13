import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, NoEntryPointError
import json
import sys
from termcolor import colored
from pretty_help import PrettyHelp


client = commands.Bot(command_prefix=["ro ", "Ro ", "ro!", "Ro!"], activity=discord.Game(name="ro help"), help_command=PrettyHelp())  # yes I know I can use case_insensitive but it doesn't work
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
    client.load_extension("extensions.leveling")
    print(f"[{DEBUG}] Leveling extension loaded.")
    client.load_extension("extensions.chat.chatFilter")
    print(f"[{DEBUG}] Chat Filter extensions loaded.")
    
except ExtensionAlreadyLoaded:
    print(f"[{WARNING}] Cog Already loaded.")


except NoEntryPointError:
    raise "[FATAL] Cog does not have a setup function!"

except ExtensionFailed as err:
    try:
        with open("DEBUG/TRACE.txt", "x"):
            print(f"[{DEBUG} Created TRACE.txt]")
    except FileExistsError:
        pass  # I know this isn't good practice but whatever
    
    with open("DEBUG/TRACE.txt", "w") as f:
        f.append(err)
        
    raise f"[{FATAL}] Extension failed loading (runtime error)! Traceback was stored in DEBUG/TRACE.txt"


client.run(settings["token"])
