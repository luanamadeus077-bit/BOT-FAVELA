import discord
from discord.ext import commands
import os

# Permissão para ler mensagens
intents = discord.Intents.default()
intents.message_content = True

# Prefixo do bot, aqui usamos !
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento quando o bot fica online
@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

# Comando de teste
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Rodar o bot usando o token das variáveis de ambiente
bot.run(os.getenv("DISCORD_TOKEN"))
