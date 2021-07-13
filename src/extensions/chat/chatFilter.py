import asyncio
import discord
from discord.ext import commands
import json


enabled = True


class chatFilter(commands.Cog):
    def __init__(self, bot:commands.Bot):
        """__init__

        Args:
            bot (module): bot instance
        """
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        """Checks each message sent for bad words

        Args:
            message (string): Discord message body

        Returns:
            integer: Exit code
        """
        global enabled
        if enabled is True:
            with open("./src/extensions/chat/badWords.json", "r") as outFile:
                bWordsList = json.load(outFile)
            if message.content.lower() in bWordsList["bad-words"]:
                await message.delete()              
                embed = discord.Embed(title=f"You are not allowed ro say that, {message.author.name}", description="These types of words are against our rules and will not be tolerated", color=0xff0000)                
                await message.channel.send(embed=embed, delete_after=10)
                await message.channel.send(f"?warn {message.author.mention}", delete_after=10)
                await asyncio.sleep(1)
                #  await message.channel.send("Dyno my man", delete_after=10)
        else:
            return 0
        
    
    @commands.group()
    async def wordfilter(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Availible commands for **Word Filter**:tm:")
            embed.add_field(title="enable", description="Enable the Word Filter:tm: \n Usage: ```!wordfilter enable```", inline=True)
            embed.add_field(title="disable", description="Disable the Word Filter:tm: \n Usage: ```!wordfilter disable```", inline=True)
            await ctx.channel.send(embed=embed)
    
    
    @wordfilter.command()
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx):
        """Disables the Word Filter

        Args:
            ctx (any): context
        """
        global enabled
        if enabled is True:
            await ctx.channel.send("Are you sure you want to disable the word filter? (yes/no)")
            confirm = commands.wait_for("message", timeout=30)
            if confirm.content.lower() == "yes":
                enabled = False
                await ctx.channel.send("Alright! The word filter is now **off**")
            else:
                await ctx.channel.send("OK! The word filter remains **on**")
                return 0
        else:
            await ctx.channel.send("BRUH. The word filter is already disabled!")
            return 0
            
            
    @wordfilter.command()
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx):
        """Enables the Word Filter

        Args:
            ctx (any): context
        """
        global enabled
        if enabled is True:
            await ctx.channel.send("Are you sure you want to disable the word filter? (yes/no)")
            confirm = commands.wait_for("message", timeout=30)
            if confirm.content.lower() == "yes":
                try:
                    enabled = True
                    await ctx.channel.send("Alright! The word filter is now **on**")
                except Exception:
                    embed = discord.Embed(title="Oops! Something went wrong!", description="FYI, here's the error: \n ```{err}```")
                    await ctx.channel.send(embed=embed)
                    return 0
            else:
                await ctx.channel.send("OK! The word filter remains **off**")
                return 0
        else:
            await ctx.channel.send("BRUH. The word filter is already enabled!")
            return 0
        

            
def setup(bot:commands.Bot):
    bot.add_cog(chatFilter(bot))
