from redbot.core import commands
import subprocess
class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startbots(self, ctx):
        """This does stuff!"""
        #owner = ctx.fetch_user(560181647006367794)
        if commands.is_owner():
            subprocess.Popen(['python3', '~/OtherBots/FRIDAY.py'])
            subprocess.Popen(['python3', '~/OtherBots/SleepBot.py'])
            subprocess.Popen(['python3','~/OtherBots/Heath.py'])
            await ctx.author.send("Bots have started!")
        else:
            ctx.send("You are not the owner")
