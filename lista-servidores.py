import discord


bot = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
        print(guild.id)


bot.run('TOKEN')
