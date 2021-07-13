import discord
from discord.ext import commands
import json


class chatFilter(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        global enabled
        enabled = True


    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        """Checks each message sent for bad words

        Args:
            message (string): Discord message body

        Returns:
            integer: Exit code
        """
        if enabled == True:
            with open("./src/extensions/chat/badWords.json", "r") as outFile:
                json.load(outFile)
                bWordsList = outFile["bad-words"]
            if message.content.lower() in bWordsList:
                message.delete()
                embed = discord.Embed(title=f"HEY {message.author.mention}", description="NO BAD WORDS :rage:", color=0xff0000)
                await message.send(f".warn {message.author.mention}")
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
    @commands.has_permissions("administrator")
    @commands.command()
    async def disable(self, ctx):
        """Disables the Word Filter

        Args:
            ctx (any): context
        """
        if enabled == True:
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
    @commands.has_permissions("administrator")
    @commands.command()
    async def enable(self, ctx):
        """Enables the Word Filter

        Args:
            ctx (any): context
        """
        if enabled == True:
            await ctx.channel.send("Are you sure you want to disable the word filter? (yes/no)")
            confirm = commands.wait_for("message", timeout=30)
            if confirm.content.lower() == "yes":
                try:
                    enabled == True
                    await ctx.channel.send("Alright! The word filter is now **on**")
                except Exception as err:
                    embed = discord.Embed(title="Oops! Something went wrong!", description="FYI, here's the error: \n ```{err}```")
                    return 0
            else:
                await ctx.channel.send("OK! The word filter remains **off**")
                return 0
        else:
            await ctx.channel.send("BRUH. The word filter is already enabled!")
            return 0
        

            
def setup(bot:commands.Bot):
    bot.add_cog(chatFilter(bot))
