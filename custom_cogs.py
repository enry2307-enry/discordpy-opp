import discord
from discord.ext import commands

# you can create multiple classes for the multiple cogs you need
class General_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # add your commands here like I did
    @commands.command()
    async def status(self, ctx):
        await ctx.send('Bot is online!')

class OtherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # add your commands here like I did
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')