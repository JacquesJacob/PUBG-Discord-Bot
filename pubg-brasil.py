import discord
import requests

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')


@client.event
async def on_message(message):
    if message.content.lower().startswith('!fpp'):
        try:
            cont = str(message.content[5:]).strip(' ')
            api_key = "TOKEN_PUBG_API"
            header = {"Authorization": "Bearer {}".format(api_key),
                      "Accept": "application/vnd.api+json"}
            url = "https://api.pubg.com/shards/steam/players?filter[playerNames]={}".format(cont)
            response = requests.get(url, headers=header)
            js = response.json()
            js2 = js['data'][0]
            js3 = js2['id']
            link = "https://api.pubg.com/shards/steam/seasons"
            reponse2 = requests.get(url=link, headers=header)
            jso = reponse2.json()
            jso2 = jso['data'][0]['id']
            link2 = 'https://api.pubg.com/shards/steam/players/{}/seasons/division.bro.official.pc-2018-07/ranked'.format(js3)
            response3 = requests.get(link2, headers=header)
            json1 = response3.json()
            json2 = json1['data']['attributes']['rankedGameModeStats']
            json3 = json2['squad-fpp']

            rankPSquad = json3['currentRankPoint']

            bronze = ':third_place: (bronze)'
            prata = ':second_place: (prata)'
            ouro = ':first_place: (ouro)'
            platinum = ':diamond_shape_with_a_dot_inside: (platinum)'
            diamond = ':gem: (diamond)'
            elite = ':star:️ (elite)'
            master = ':trophy: (master)'
            grandmaster = ':crown: (grandmaster)'

            SquadPlayed = int(json3['bestRankPoint'])

            if SquadPlayed <= 9:
                rankPSquad = 0
                Squad = '(menos de 10 partidas)'

            else:

                if rankPSquad <= 1699:
                    Squad = bronze

                elif rankPSquad >= 2000 and rankPSquad <= 2299:
                    Squad = ouro

                elif rankPSquad >= 1700 and rankPSquad <= 1999:
                    Squad = prata

                elif rankPSquad >= 2300 and rankPSquad <= 2599:
                    Squad = platinum

                elif rankPSquad >= 2600 and rankPSquad <= 2999:
                    Squad = diamond

                elif rankPSquad >= 3000 and rankPSquad <= 3399:
                    Squad = elite

                elif rankPSquad >= 3400 and rankPSquad <= 4999:
                    Squad = master

                else:
                    Squad = grandmaster

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
                                                "Media Rank: {}\n"
                                                "Vitórias: {}\n"
                                                "Pontos Atual: {} {}\n"
                                                "----------------------\n".format(
                                                                                  cont,
                                                                                  json3['roundsPlayed'],
                                                                                  json3['kills'],
                                                                                  json3['assists'],
                                                                                  kda,
                                                                                  top10Ratio,
                                                                                  avgRank,
                                                                                  json3['wins'],
                                                                                  rankPSquad, Squad
                                                                                  ))
            EmbedPu.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
            EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')
            await client.send_message(message.channel, embed=EmbedPu)


        except KeyError:
            await client.send_message(message.channel, "Não foi possivel encontrar este jogador! Verifique se o "
                                                       "NickName esta correto!")


client.run('TOKEN_BOT_DISCORD')
