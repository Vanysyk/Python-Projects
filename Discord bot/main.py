import discord
from discord.ext import commands
from config import settings
import json
import requests

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def hello(arg):
    author = arg.message.author
    await arg.send(f'Hello, {author.mention}!')

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run(settings['token'])

