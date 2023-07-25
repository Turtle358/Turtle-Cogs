from redbot.core import commands
import subprocess
class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startbots(self, ctx):
        """This does stuff!"""
        owner = ctx.get_user(560181647006367794)
        if ctx.author.id == 560181647006367794:
            subprocess.Popen(['python3', '~/OtherBots/FRIDAY.py'])
            subprocess.Popen(['python3', '~/OtherBots/SleepBot.py'])
            subprocess.Popen(['python3','~/OtherBots/Heath.py'])
            await owner.send("Bots have started!")
        else:
            ctx.send("You are not the owner")