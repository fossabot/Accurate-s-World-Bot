import discord
from discord.ext import commands
import json


client = commands.Bot(command_prefix="!")
with open("src/SECRET.json", "r")as f:
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
        

client.run(settings["token"])
