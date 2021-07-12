import discord
from discord.ext import commands
import json


class chatFilter(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        """Checks each message sent for bad words

        Args:
            message (string): Discord message body

        Returns:
            integer: Exit code
        """
        with open("./src/extensions/chat/badWords.json", "r") as f:
            json.load(f)
            bWordsList = f["bad-words"]
        if message.content.lower() in bWordsList:
            message.delete()
            embed=discord.Embed(title=f"HEY {message.author.mention}", description="NO BAD WORDS :rage:", color=0xff0000)
            await message.send(f"?warn {message.author.mention}")
            
            async def on_message(message):
                if message.author.name == "Dyno":
                    await message.reply("thanks fam :sunglasses:")
                    return 0
            
    
    


def setup(bot:commands.Bot):
    bot.add_cog(chatFilter(bot))