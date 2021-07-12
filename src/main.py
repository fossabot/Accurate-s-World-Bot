import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, NoEntryPointError


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is online")


@client.event
async def on_message(message):
    """Checks for AMOGUS

    Args:
        message (string): message

    Returns:
        integer: Exit code
    """
    if message.channel.name == "we-love-amogus":
        if "amogus" not in message.content.lower():
            try:
                message.delete()
            except Exception as err:
                embed = discord.Embed(title="R.I.P Something went wrong!",
                                    description=f"if you're developer, here's the traceback. ```{err}```")
                return 1
            
            await message.channel.send("ONLY AMOGUS :rage: :rage:")
            await message.channel.send(f"?warn {message.author.display_name}")
            return 0
        else:
            return
    else:
        return 0
        
        
@client.command(name="ping", brief="Display Bot ping")
async def get_ping(ctx):
    """Gets Bot Ping

    Args:
        ctx (any): context

    Returns:
        integer: Exit code
    """
    
    embed = discord.Embed(title="Pong!", description=client.latency + "ms",)
    await ctx.channel.send(embed=embed)
    return 0
    
        
try:
    client.load_extension("src\extensions\leveling.py")
    
except ExtensionAlreadyLoaded:
    print("[WARN] Cog Already loaded.")

except NoEntryPointError:
    raise "[FATAL] Cog does not have a setup function!"

except ExtensionFailed as err:
    with open("DEBUG/TRACE.txt", "w") as f:
        f.append(err)
        
    raise "[FATAL] Extension failed loading (runtime error)! Traceback was stored in DEBUG/TRACE.txt"


client.run("")  # <- token goes here
