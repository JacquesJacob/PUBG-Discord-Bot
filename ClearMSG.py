import discord
import asyncio
from discord.ext import commands
from discord.utils import get

client = discord.Client()

Client = commands.Bot(command_prefix=".")


@Client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@Client.command()
async def clear(ctx, numero: int):
    role_adm = discord.utils.get(ctx.guild.roles, name="BOT Manager")
    role_sup = discord.utils.get(ctx.guild.roles, name="Staff")
    if role_adm in ctx.author.roles or role_sup in ctx.author.roles:
        await ctx.channel.send("Removendo mensagens...")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=numero+2)
        print("mensagem deletada com sucesso!")
    else:
        await ctx.channel.send("Você não tem permissão para executar este comando!")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=2)
        print("mensagem nao pode ser deletada!")


Client.run('TOKEN_BOT_DISCORD')

