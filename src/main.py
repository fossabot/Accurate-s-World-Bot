import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, NoEntryPointError
import json
import sys
from termcolor import colored
from pretty_help import PrettyHelp
import random
import requests


client = commands.Bot(command_prefix=["ro ", "Ro ", "ro!", "Ro!"], activity=discord.Game(name="ro help!"))  # yes I know I can use case_insensitive but it doesn't work
client.help_command = PrettyHelp(ending_note="[CLASSIFIED]", show_index=False, no_category="Misc")
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


@client.command(name="coinflip", brief="Heads or tails? Flip the coin!")
async def coinflip(ctx, *args, **kwargs):
    """Chooses between heads or tails.

    Args:
        ctx (any): Context

    Returns:
    integer: Exit code
    """
    possibilities = ["Tails", "Heads"]
    embed = discord.Embed(title=random.choice(possibilities) + " !", set_image="https://w7.pngwing.com/pngs/724/435/png-transparent-dollar-coin-computer-icons-drawing-coin-gold-coin-gold-number.png")
    await ctx.channel.send(embed=embed)
    return 0
  
  
@client.command(name="die", brief="Die.")
async def die(ctx):
    ctx.message.channel.send("You're dead now.")
    return 0


@client.command(name="joke")
async def joke(ctx):
    def jokes(f):
        data = requests.get(f)
        tt = json.loads(data.text)
        return tt
    
    f = r"https://official-joke-api.appspot.com/random_joke"
    a = jokes(f)
    
    for i in (a):
        print(i["type"])
        print(i["setup"])
        print(i["punchline"],)
    embed = discord.Embed(title="Jokes")    
  
        
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
