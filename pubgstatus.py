import discord
import requests
import mysql.connector

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.event
async def on_message(message):

    if message.content.lower().startswith('!pubg'):
      try:
        cont = str(message.content[6:]).strip(' ')
        api_key = "API_TOKEN"
        header = {
            "Authorization": "Bearer {}".format(api_key),
            "Accept": "application/vnd.api+json"
        }
        url = "https://api.pubg.com/shards/pc-sa/players?filter[playerNames]={}".format(cont)
        response = requests.get(url, headers=header)
        js = response.json()
        js2 = js['data'][0]
        js3 = js2['id']
        link = "https://api.pubg.com/shards/steam/seasons"
        reponse2 = requests.get(url=link, headers=header)
        jso = reponse2.json()
        jso2 = jso['data'][0]['id']
        link2 = 'https://api.pubg.com/shards/steam/players/{}/seasons/division.bro.official.pc-2018-01'.format(js3)
        response3 = requests.get(link2, headers=header)
        json1 = response3.json()
        json2 = json1['data']['attributes']['gameModeStats']
        json3 = json2['solo']
        json4 = json2['duo']
        json5 = json2['squad']

        KDSolo = round(json3['kills'] / json3['losses'], 2)
        KDDuo = round(json4['kills'] / json4['losses'], 2)
        KDSquad = round(json5['kills'] / json5['losses'], 2)

        rankPSolo = json3['rankPoints']
        rankPSolo = int(rankPSolo)
        rankPDuo = json4['rankPoints']
        rankPDuo = int(rankPDuo)
        rankPSquad = json5['rankPoints']
        rankPSquad = int(rankPSquad)

        bronze = ':third_place: (bronze)'
        prata = ':second_place: (prata)'
        ouro = ':first_place: (ouro)'
        platinum = ':military_medal: (platinum)'
        diamond = ':gem: (diamond)'
        elite = ':medal: (elite)'
        master = ':medal: :medal: (master)'
        grandmaster = ':trophy: (grandmaster)'

        SoloPlayed = json3['roundsPlayed']
        DuoPlayed = json4['roundsPlayed']
        SquadPlayed = json5['roundsPlayed']

        MPointsSolo = int(json3['bestRankPoint'])
        MPointsDuo = int(json4['bestRankPoint'])
        MPointsSquad = int(json5['bestRankPoint'])

        if SoloPlayed <= 9:
            rankPSolo = 0
            Solo = '(menos de 10 partidas)'
        elif rankPSolo <= 1399:
                Solo = bronze
        elif rankPSolo >= 1500 and rankPSolo <= 1599:
                Solo = ouro
        elif rankPSolo >= 1400 and rankPSolo <= 1499:
                Solo = prata
        elif rankPSolo >= 1600 and rankPSolo <= 1699:
                Solo = platinum
        elif rankPSolo >= 1700 and rankPSolo <= 1799:
                Solo = diamond
        elif rankPSolo >= 1800 and rankPSolo <= 1899:
                Solo = elite
        elif rankPSolo >= 1900 and rankPSolo <= 1999:
                Solo = master
        else:
                Solo = grandmaster


        if DuoPlayed <= 9:
            rankPDuo = 0
            Duo = '(menos de 10 partidas)'
        elif rankPDuo <= 1399:
            Duo = bronze
        elif rankPDuo >= 1500 and rankPDuo <= 1599:
            Duo = ouro
        elif rankPDuo >= 1400 and rankPDuo <= 1499:
            Duo = prata
        elif rankPDuo >= 1600 and rankPDuo <= 1699:
            Duo = platinum
        elif rankPDuo >= 1700 and rankPDuo <= 1799:
            Duo = diamond
        elif rankPDuo >= 1800 and rankPDuo <= 1899:
            Duo = elite
        elif rankPDuo >= 1900 and rankPDuo <= 1999:
            Duo = master
        else:
            Duo = grandmaster


        if SquadPlayed <= 9:
            rankPSquad = 0
            Squad = '(menos de 10 partidas)'
        elif rankPSquad <= 1399:
            Squad = bronze
        elif rankPSquad >= 1500 and rankPSquad <= 1599:
            Squad = ouro
        elif rankPSquad >= 1400 and rankPSquad <= 1499:
            Squad = prata
        elif rankPSquad >= 1600 and rankPSquad <= 1699:
            Squad = platinum
        elif rankPSquad >= 1700 and rankPSquad <= 1799:
            Squad = diamond
        elif rankPSquad >= 1800 and rankPSquad <= 1899:
            Squad = elite
        elif rankPSquad >= 1900 and rankPSquad <= 1999:
            Squad = master
        else:
            Squad = grandmaster



        EmbedPu = discord.Embed(title="PlayerUnknown's Battlegrounds\n"
                                      "Servers WW | TPP | New Season 1",
                                description="----------------------\n"
                                            "Player: {}\n"
                                            "----------------------\n"
                                            "Solo\n"
                                            "Partida(s): {}\n"
                                            "Kills: {}\n"
                                            "K/D: {}\n"
                                            "Assistencias: {}\n"
                                            "Record Kills em partida: {}\n"
                                            "Kills por Headshot: {}\n"
                                            "Top 10: {}\n"
                                            "Vitórias: {}\n"
                                            "Pontos Max: {}\n"
                                            "Pontos Atual: {} {}\n"
                                            "----------------------\n"
                                            "Duo\n"
                                            "Partida(s): {}\n"
                                            "Kills: {}\n"
                                            "K/D: {}\n"
                                            "Assistencias: {}\n"
                                            "Record Kills em partida: {}\n"
                                            "Kills por Headshot: {}\n"
                                            "Top 10: {}\n"
                                            "Vitórias: {}\n"
                                            "Pontos Max: {}\n"
                                            "Pontos Atual: {} {}\n"
                                            "----------------------\n"
                                            "Squad\n"
                                            "Partida(s): {}\n"
                                            "Kills: {}\n"
                                            "K/D: {}\n"
                                            "Assistencias: {}\n"
                                            "Record Kills em partida: {}\n"
                                            "Kills por Headshot: {}\n"
                                            "Top 10: {}\n"
                                            "Vitórias: {}\n"
                                            "Pontos Max: {}\n"
                                            "Pontos Atual: {} {}\n"
                                            "----------------------\n".format(
                                                        cont,
                                                        json3['roundsPlayed'],
                                                        json3['kills'],
                                                        KDSolo,
                                                        json3['assists'],
                                                        json3['roundMostKills'],
                                                        json3['headshotKills'],
                                                        json3['top10s'],
                                                        json3['wins'],
                                                        MPointsSolo,
                                                        rankPSolo, Solo,
                                                        json4['roundsPlayed'],
                                                        json4['kills'],
                                                        KDDuo,
                                                        json4['assists'],
                                                        json4['roundMostKills'],
                                                        json4['headshotKills'],
                                                        json4['top10s'],
                                                        json4['wins'],
                                                        MPointsDuo,
                                                        rankPDuo, Duo,
                                                        json5['roundsPlayed'],
                                                        json5['kills'],
                                                        KDSquad,
                                                        json5['assists'],
                                                        json5['roundMostKills'],
                                                        json5['headshotKills'],
                                                        json5['top10s'],
                                                        json5['wins'],
                                                        MPointsSquad,
                                                        rankPSquad, Squad
                                                                            ))
        EmbedPu.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
        EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')
        await client.send_message(message.channel, embed=EmbedPu)

        ######### CONEXAO COM O BANCO DE DADOS MYSQL ##############

        cnx = mysql.connector.connect(user='user', database='db', port='3306', host='host_db',
                                      password='password')

        cursor = cnx.cursor()

        pubg_name = cont
        solo_points = rankPSolo
        duo_points = rankPDuo
        squad_points = rankPSquad

        insert = """
                    INSERT INTO pubgdiscord (pubg_name, solo_points, duo_points, squad_points)
                    VALUES (%s, %s, %s, %s) 
                    ON DUPLICATE KEY UPDATE   
                    solo_points=%s, duo_points=%s, squad_points=%s
                 """

        cursor.execute(insert, (pubg_name, solo_points, duo_points, squad_points, solo_points, duo_points, squad_points))

        cnx.commit()
        cursor.close()
        cnx.close()

        ######### FIM CONEXAO COM O BANCO DE DADOS MYSQL ##############

      except KeyError:
          await client.send_message(message.channel, "Não foi possivel encontrar este jogador! Verifique se o "
                                                     "NickName esta correto!")

client.run('API_TOKEN')
