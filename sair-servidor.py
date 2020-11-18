import discord
from discord import Guild

client = discord.Client()


@client.event
async def on_ready():
    my_server = client.get_guild(ID-SERVIDOR-PARA-SAIR)
    await Guild.leave(my_server)

client.run('TOKEN')
