import discord
from discord.ext import commands
import os

# Permissão para ler mensagens
intents = discord.Intents.default()
intents.message_content = True

# Prefixo do bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Rodar o bot usando a variável de ambiente
bot.run(os.getenv("DISCORD_TOKEN"))
