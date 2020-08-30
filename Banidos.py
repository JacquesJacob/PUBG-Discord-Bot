import discord
from discord.ext import commands
import asyncio

client = discord.Client()

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')


@bot.command()
async def lista_banidos(ctx):
    role_adm = discord.utils.get(ctx.guild.roles, name="BOT Manager")
    role_sup = discord.utils.get(ctx.guild.roles, name="🔰 Staff")
    if role_adm in ctx.author.roles or role_sup in ctx.author.roles:
        bans = await ctx.guild.bans()
        pretty_list = ["• {0.id} ({0.name}#{0.discriminator})".format(entry.user) for entry in bans]
        #await ctx.send("**Ban list:** \n{}".format("\n".join(pretty_list)))
        print("**Ban list:** \n{}".format("\n".join(pretty_list)))
        #EmbedPu = discord.Embed(title="Lista de Usuários Banidos:", description="{}\n".join(pretty_list))
        #await ctx.channel.send(embed=EmbedPu)


bot.run('BOT_TOKEN')
