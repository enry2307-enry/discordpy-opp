import discord
from discord.ext import commands
from datetime import datetime

from custom_cogs import General_commands, OtherCommands # for the custom cogs

intents = discord.Intents.default()
intents.message_content = True

""" Extending bot's class """
class Bot(commands.Bot):
        def __init__(self, command_prefix, intents, self_bot=False):
            commands.Bot.__init__(self, command_prefix=command_prefix, intents=intents, self_bot=self_bot)

        """ Overriding this method allows to add cogs """
        async def setup_hook(self):
            await self.add_cog(General_commands(self)) # write this line for any cog class you added
            await self.add_cog(OtherCommands(self))

        """ This method is called when the bot is ready """
        async def on_ready(self):
            print(f'Bot is online - {datetime.today().strftime("Date %Y-%m-%d | Time %H:%M:%S ( Server Datetime ) ")}')

        """ This method is called when any user sends a message """
        async def on_message(self, message):
            await self.process_commands(message)

bot = Bot(command_prefix="!", intents=intents)
bot.run("token")

# invite link
# https://discord.com/api/oauth2/authorize?client_id=PUBLIC_KEY&permissions=0&scope=bot%20applications.commands