import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
import json
from json import JSONDecodeError
from datetime import datetime
from sys import exit
from main import DEBUG, WARNING, FATAL


class leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Adds points to a user

        Args:
            message (string): Discord message body
        """
        
        global userName
        global levelsFile
        userName= str(message.author.name)
        
        with open("src\extensions\levels.json", "r", encoding="utf-8") as outFile:  # opens the file where levels are contained
            levelsFile = json.load(outFile)
            
            if userName not in levelsFile:
                try :
                    levelsFile[userName] = 0
                    print(f"[{DEBUG}] Registered new key for {userName}")
                except  Exception:
                    print(f"[{FATAL}] Could not register key. Level cog halted.")
                    exit(1)
            
        with open("src\extensions\levels.json", "w") as outFile:
            levelsFile[userName] += 1
            json.dump(levelsFile, outFile, indent=4)
            
                    
    
    
    @commands.command()
    async def level(self, ctx, *args, **kwargs):
        """
        rounds the points to the nearest 10, then divides it by ten. Example Below.
        example: if the points are equal to 23, then the level is 2. And considering this, this also means that 26 points is equal to level 3.
        This means that a level is equal to roughly ~7 points.
        """
        
        try:
            with open("src\extensions\levels.json", "r") as outFile:
                points = json.load(outFile)
            userLevel = round(levelsFile[userName] / 10) * 10 / 10  # calculates the level with the points given
            int(userLevel)
            embed = discord.Embed(title="Level", description=f"Currently, your level is {userLevel}. ({points[userName]} points)", color=0x3514db)  # sends it in an embed
            await ctx.channel.send(embed=embed)
        except CommandInvokeError:
            return 1
            


def setup(bot):
    bot.add_cog(leveling(bot))  # registers cog
