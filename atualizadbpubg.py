import mysql.connector
import requests
import time

cnx = mysql.connector.connect(user='USER', database='DATABASE', port='3306',
                              host='IP',
                              password='PASSWORD')

cursor = cnx.cursor()

query = ("SELECT pubg_name FROM pubgdiscord")

cursor.execute(query)

while True:

  try:

    while True:

        for row in cursor:

            nome = format(row).split("'")[1]

            api_key = "TOKEN" \
            header = {
                        "Authorization": "Bearer {}".format(api_key),
                        "Accept": "application/vnd.api+json"
                     }
            url = "https://api.pubg.com/shards/pc-sa/players?filter[playerNames]={}".format(nome)

            response = requests.get(url, headers=header)
            js = response.json()
            js2 = js['data'][0]
            js3 = js2['id']
            link = "https://api.pubg.com/shards/pc-sa/seasons"

            reponse2 = requests.get(url=link, headers=header)
            jso = reponse2.json()
            jso2 = jso['data'][0]['id']
            link2 = 'https://api.pubg.com/shards/pc-sa/players/{}/seasons/division.bro.official.2018-09'.format(js3)

            response3 = requests.get(link2, headers=header)
            json1 = response3.json()
            json2 = json1['data']['attributes']['gameModeStats']
            json3 = json2['solo']
            json4 = json2['duo']
            json5 = json2['squad']

            PontosSolo = json3['winPoints']
            PontosDuo = json4['winPoints']
            PontosSquad = json5['winPoints']

            KillPSolo = json3['killPoints']
            KillPDuo = json4['killPoints']
            KillPSquad = json5['killPoints']

            PSolo = KillPSolo * 0.2 + PontosSolo
            PSolo4 = int(PSolo)
            PDuo = KillPDuo * 0.2 + PontosDuo
            PDuo4 = int(PDuo)
            PSquad = KillPSquad * 0.2 + PontosSquad
            PSquad4 = int(PSquad)

            print(nome, PSolo4, PDuo4, PSquad4)

            cnx2 = mysql.connector.connect(user='USER', database='DATABASE', port='3306',
                                       host='IP',
                                       password='PASSWORD')

            cursor2 = cnx2.cursor()

            pubg_name = nome
            solo_points = PSolo4
            duo_points = PDuo4
            squad_points = PSquad4

            insert = """
                    INSERT INTO pubgdiscord (pubg_name, solo_points, duo_points, squad_points)
                    VALUES (%s, %s, %s, %s) 
                    ON DUPLICATE KEY UPDATE   
                    solo_points=%s, duo_points=%s, squad_points=%s
                 """

            cursor2.execute(insert, (pubg_name, solo_points, duo_points, squad_points, solo_points, duo_points, squad_points))

            cnx2.commit()
            cursor2.close()
            cnx2.close()

            time.sleep(20)


    cnx.commit()
    cursor.close()
    cnx.close()

    print("Update concluido. Iniciando contagem de 11000 segundos para proxima atualizacao.")

    time.sleep(11000)

  except KeyError:
        print("Erro para consultar o jogador {}. Verifique se ainda existe.".format(nome))
        time.sleep(15)
