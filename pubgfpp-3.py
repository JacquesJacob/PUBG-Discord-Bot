import discord
import requests

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "rank" in message.channel.name:

        if message.content.startswith('!fpp'):

            try:
                cont = str(message.content[5:]).strip(' ')
                api_key = "PUBG_API_TOKEN"
                header = {"Authorization": "Bearer {}".format(api_key), "Accept": "application/vnd.api+json"}
                url = "https://api.pubg.com/shards/steam/players?filter[playerNames]={}".format(cont)
                response = requests.get(url, headers=header)
                js = response.json()
                js2 = js['data'][0]
                js3 = js2['id']
                link = "https://api.pubg.com/shards/steam/seasons"
                reponse2 = requests.get(url=link, headers=header)
                jso = reponse2.json()
                jso2 = jso['data'][0]['id']
                link2 = 'https://api.pubg.com/shards/steam/players/{}/seasons/division.bro.official.' \
                        'pc-2018-08/ranked'.format(js3)
                response3 = requests.get(link2, headers=header)
                json1 = response3.json()
                json2 = json1['data']['attributes']['rankedGameModeStats']
                json3 = json2['squad-fpp']

                rankPSquad = json3['currentRankPoint']

                bronze = ':third_place:'
                prata = ':second_place:'
                ouro = ':first_place:'
                platinum = ':diamond_shape_with_a_dot_inside:'
                diamond = ':gem:'
                master = ':trophy:'

                SquadPlayed = int(json3['bestRankPoint'])
                if SquadPlayed <= 9:
                    rankPSquad = 0
                    Squad = '(menos de 10 partidas)'

                else:

                    tier = json3['currentTier']
                    if rankPSquad <= 1499:
                        Squad = bronze
                    elif rankPSquad >= 2000 and rankPSquad <= 2499:
                        Squad = ouro
                    elif rankPSquad >= 1500 and rankPSquad <= 1999:
                        Squad = prata
                    elif rankPSquad >= 2500 and rankPSquad <= 2999:
                        Squad = platinum
                    elif rankPSquad >= 3000 and rankPSquad <= 3499:
                        Squad = diamond
                    else:
                        Squad = master

                tier = json3['currentTier']
                kda = round(json3['kda'], 2)
                top10Ratio = round(json3['top10Ratio'], 2)
                avgRank = round(json3['avgRank'], 2)
                EmbedPu = discord.Embed(title="PlayerUnknown's Battlegrounds\n"
                                              "Servers WW | FPP | RANKED",
                                        description="----------------------\n"
                                                    "Player: {}\n"
                                                    "----------------------\n"
                                                    "Squad\n"
                                                    "Partida(s): {}\n"
                                                    "Kills: {}\n"
                                                    "Assistencias: {}\n"
                                                    "KDA: {}\n"
                                                    "Top 10 Taxa: {}\n"
                                                    "Media Posicao: {}\n"
                                                    "Vitórias: {}\n"
                                                    "Pontos Atual: {}\n"
                                                    "----------------------\n"
                                                    "Rank: {} {} {} {}\n"
                                                    "----------------------\n".format(
                                            cont,
                                            json3['roundsPlayed'],
                                            json3['kills'],
                                            json3['assists'],
                                            kda,
                                            top10Ratio,
                                            avgRank,
                                            json3['wins'],
                                            rankPSquad, Squad,
                                            tier["tier"],
                                            tier["subTier"],
                                            Squad
                                        ))
                EmbedPu.add_field(name="Nos ajude no desenvolvimento deste Bot!",
                                  value=":arrow_down: Doe qualquer valor clicando abaixo. :arrow_down:\n"
                                        "https://paypal.me/JACQUESJacob")
                EmbedPu.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
                EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')
                await message.channel.send(embed=EmbedPu)

            except KeyError:
                await message.channel.send("Não foi possivel encontrar este Player! "
                                           "Verifique se digitou o Nickname corretamente. ")

    else:
        await message.channel.send("Favor executar este comando no canal #rank! Obrigado!")


client.run('DISCORD_BOT_TOKEN')
