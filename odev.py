import discord
import requests
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, çevreye duyarlı bir Discord botuyum!')


@bot.command()
async def bilgi(ctx):
    await ctx.send(f'Ne hakkında bilgi almak istiyorsun?')
    time.sleep(1)
    await ctx.send(f"Plastik Atıklar (.plastik)")
    time.sleep(1)
    await ctx.send(f"Camlar Atıklar (.cam)")
    time.sleep(1)
    await ctx.send(f"Kâğıt / Karton Atıklar (.kagit)")


@bot.command()
async def plastik(ctx):
    await ctx.send(f"Plastik atıklar çok uzun sürede toprağa karışırlar. ")
    time.sleep(1)
    await ctx.send(f"Bu yüzden geri dönüştürülmesi gerekmektedir.")
    time.sleep(1)
    await ctx.send(f"Plastik atıkların geri dönüşüm kutusu sarı renklidir")
    time.sleep(1)
    with open('geridonusumkutusu\plastik.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def cam(ctx):
    await ctx.send(f"Cam atıklar doğada yaklaşık 4000 yıl durabilir.")
    time.sleep(1)
    await ctx.send(f"Bu yüzden geri dönüştürülmesi gerekir.")
    time.sleep(1)
    await ctx.send(f"Cam atıkların geri dönüşüm kutusu yeşil renktedir.")
    time.sleep(1)
    with open('geridonusumkutusu\cam.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def kagit(ctx):
    await ctx.send(f"Kağıtlar ağaçlardan yapılır ve ne kadar harcanırsa o kadar ağaç kesilir.")
    time.sleep(1)
    await ctx.send(f"Bu yüzden geri dönüştürülmesi gerekir.")
    time.sleep(1)
    await ctx.send(f"Kağıt atıkların geri dönüşüm kutusu mavi renklidir.")
    time.sleep(1)
    with open('geridonusumkutusu\kagit.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("TOKEN")
