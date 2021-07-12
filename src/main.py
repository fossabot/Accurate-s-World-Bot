import discord
from discord.ext import commands
import json


client = commands.Bot(command_prefix="!")
with open("SECRET.json", "r")as f:
    settings = json.load(f)


@client.event
async def on_ready():
    print("Bot is online")


@client.event
async def on_message(message):
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
        

client.run(settings["token"])
