import discord
from discord.ext import commands
from manage.settings import bot_connect_data


settings = bot_connect_data()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


class GetPlayerData:
    def __init__(self, unit):
        self.unit = unit
        self.version = '3.3.5'


@bot.command()
async def rand(ctx, *arg):
    data = GetPlayerData(unit = arg[0])
    await ctx.reply(data.unit)

bot.run(settings['token'])
