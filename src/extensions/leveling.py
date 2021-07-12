import discord
from discord.ext import commands
import json
from datetime import datetime


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
        global userRegistered  # declares global variables to be used throughout the file
        global levelsFile
        userName= message.author.name 
        
        with open("levels.json", "a+") as levelsFile:# opens the file where levels are contained
            json.load(levelsFile)
            if userName in levelsFile:
                userRegistered = True
            else:
                levelsFile[userName] = 0
        levelsFile[userName] ++ 1
    
    
    @commands.command(name="level", brief="Get your current level.")
    async def get_level(self):
        """
        rounds the points to the nearest 10, then divides it by ten. Example Below.
        example: if the points are equal to 23, then the level is 2. And considering this, this also means that 26 points is equal to level 3.
        This means that a level is equal to roughly ~7 points.
        """
        
        userLevel = round(levelsFile[userName] / 10) * 10  # calculates the level with the points given
        embed = discord.Embed(title="Level", description=f"Currently, your level is {userLevel}", color=0x3514db)  # sends it in an embed


def setup(bot):
    bot.add_cog(leveling(bot))  # registers cog
