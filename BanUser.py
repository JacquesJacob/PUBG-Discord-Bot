import discord
from discord.ext import commands
import asyncio

TOKEN = "DISCORD_TOKEN"

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ban(ctx, user: discord.Member, qtd_dias: int, motivo: str):
    try:
        role_adm = discord.utils.get(ctx.guild.roles, name="BOT Manager")
        role_sup = discord.utils.get(ctx.guild.roles, name="🔰 Staff")
        if role_adm in ctx.author.roles or role_sup in ctx.author.roles:
            dias = qtd_dias * 86400
            canal = await user.create_dm()
            await canal.send("Olá! Você foi banido por {} dias pelo motivo: {}. Você será automaticamente desbanido "
                             "ao final deste prazo!".format(qtd_dias, motivo))
            await ctx.guild.ban(user)
            await ctx.channel.send("Usuario {} banido com sucesso por {} dias. Ele será desbanido automaticamente "
                                   "após concluir o tempo indicado. Motivo: {}".format(user, qtd_dias, motivo))
            canal = client.get_channel(336644581603016715)
            await canal.send("Usuario {} banido por {} dias. Ele será desbanido "
                             "automaticamente após concluir o tempo indicado. "
                             "Motivo: {}".format(user, qtd_dias, motivo))
            await asyncio.sleep(dias)
            await ctx.guild.unban(user)
            await ctx.channel.send("Usuario {} desbanido após {} dias.".format(user, qtd_dias))
            await canal.send("Usuario {} desbanido após {} dias.".format(user, qtd_dias))
        else:
            await ctx.channel.send("Você não tem permissão para executar este comando.")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=2)

    except KeyError:
        await ctx.channel.send("Erro de comando! Verifique e tente novamente!")


@client.command()
async def clearall(ctx, channel: discord.TextChannel = None):
    role_adm = discord.utils.get(ctx.guild.roles, name="BOT Manager")
    role_sup = discord.utils.get(ctx.guild.roles, name="🔰 Staff")
    if role_adm in ctx.author.roles or role_sup in ctx.author.roles:
        await ctx.channel.send("Removendo mensagens...")
        await asyncio.sleep(3)
        channel = channel or ctx.channel
        count = 0
        async for _ in channel.history(limit=None):
            count += 1
        await ctx.channel.send("Removendo total de {} mensagens.".format(count))
        await asyncio.sleep(2)
        total = count + 1
        print("limpando total de {} mensagens no canal {}".format(total, channel.mention))
        await ctx.channel.purge(limit=total, check=lambda msg: not msg.pinned)
        print("mensagem deletada com sucesso!")
    else:
        await ctx.channel.send("Você não tem permissão para executar este comando!")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=2)
        print("mensagem nao pode ser deletada!")


client.run(TOKEN)
