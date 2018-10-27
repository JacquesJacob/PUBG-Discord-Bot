import discord
import mysql.connector
import re

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.event
async def on_message(message):

    if message.content.lower().startswith('!ajuda'):
            await client.send_message(message.channel, "Olá! Para consultar seu status no PUBG digite '!pubg Nickname'"
                                                       " no canal #rank.\n"
                                                       "Para consultar o rank PUBG do canal, digite: '!pubrank "
                                                       "solo' (solo - duo - squad). Qualquer duvida procure um MOD/ADM.")


    if message.content.lower().startswith('!pubrank solo'):

        if "rank" in message.channel.name:
            try:
                cnx = mysql.connector.connect(user='USER', database='DATABASE', port='3306', host='IP',
                                              password='PASSWORD')

                cursor = cnx.cursor()

                query = ("SELECT pubg_name, solo_points FROM pubgdiscord ORDER BY solo_points DESC limit 15")

                cursor.execute(query)
                starting_index = cursor.fetchall()
                starting_index_1 = str(starting_index[0])
                starting_index_2 = str(starting_index[1])
                starting_index_3 = str(starting_index[2])
                starting_index_4 = str(starting_index[3])
                starting_index_5 = str(starting_index[4])
                starting_index_6 = str(starting_index[5])
                starting_index_7 = str(starting_index[6])
                starting_index_8 = str(starting_index[7])
                starting_index_9 = str(starting_index[8])
                starting_index_dez = str(starting_index[9])
                starting_index_11 = str(starting_index[10])
                starting_index_12 = str(starting_index[11])
                starting_index_13 = str(starting_index[12])
                starting_index_14 = str(starting_index[13])
                starting_index_15 = str(starting_index[14])

                nome1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[0])
                ponto1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[1])
                nome2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[0])
                ponto2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[1])
                nome3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[0])
                ponto3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[1])
                nome4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[0])
                ponto4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[1])
                nome5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[0])
                ponto5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[1])
                nome6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[0])
                ponto6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[1])
                nome7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[0])
                ponto7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[1])
                nome8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[0])
                ponto8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[1])
                nome9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[0])
                ponto9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[1])
                nome10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[0])
                ponto10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[1])
                nome11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[0])
                ponto11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[1])
                nome12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[0])
                ponto12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[1])
                nome13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[0])
                ponto13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[1])
                nome14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[0])
                ponto14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[1])
                nome15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[0])
                ponto15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[1])

                EmbedPu = discord.Embed(title="PlayerUnknown's Battlegrounds\n"
                                              "Servers SA | TPP | Season 9\n"
                                              "\n"
                                              "Melhores 15 Jogadores Solo:")

                EmbedPu.add_field(name="Nickname", value="__1. {}__\n"
                                                         "2. {}\n"
                                                         "3. {}\n"
                                                         "4. {}\n"
                                                         "5. {}\n"
                                                         "6. {}\n"
                                                         "7. {}\n"
                                                         "8. {}\n"
                                                         "9. {}\n"
                                                         "10. {}\n"
                                                         "11. {}\n"
                                                         "12. {}\n"
                                                         "13. {}\n"
                                                         "14. {}\n"
                                                         "15. {}\n".format(nome1, nome2, nome3, nome4, nome5,
                                                                           nome6, nome7, nome8, nome9, nome10,
                                                                           nome11, nome12, nome13, nome14, nome15), inline=True)
                EmbedPu.add_field(name="Pontos", value="__{}__\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n"
                                                       "{}\n".format(ponto1, ponto2, ponto3, ponto4, ponto5, ponto6, ponto7,
                                                                     ponto8, ponto9, ponto10, ponto11, ponto12, ponto13,
                                                                     ponto14, ponto15), inline=True)

                EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
                EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')

                await client.send_message(message.channel, embed=EmbedPu)

                cnx.commit()
                cursor.close()
                cnx.close()

            except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))
                    await client.send_message(message.channel, "Erro ao consultar banco de dados {}".format(err))

        else:

            await client.send_message(message.channel, "Executar este comando no canal #rank! Obrigado!")

    if message.content.lower().startswith('!pubrank duo'):

        if "rank" in message.channel.name:

            cnx = mysql.connector.connect(user='USER', database='DATABASE', port='3306',
                                          host='HOST',
                                          password='PASSWORD')

            cursor = cnx.cursor()

            query = ("SELECT pubg_name, duo_points FROM pubgdiscord ORDER BY duo_points DESC limit 15")

            cursor.execute(query)
            starting_index = cursor.fetchall()
            starting_index_1 = str(starting_index[0])
            starting_index_2 = str(starting_index[1])
            starting_index_3 = str(starting_index[2])
            starting_index_4 = str(starting_index[3])
            starting_index_5 = str(starting_index[4])
            starting_index_6 = str(starting_index[5])
            starting_index_7 = str(starting_index[6])
            starting_index_8 = str(starting_index[7])
            starting_index_9 = str(starting_index[8])
            starting_index_dez = str(starting_index[9])
            starting_index_11 = str(starting_index[10])
            starting_index_12 = str(starting_index[11])
            starting_index_13 = str(starting_index[12])
            starting_index_14 = str(starting_index[13])
            starting_index_15 = str(starting_index[14])

            nome1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[0])
            ponto1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[1])
            nome2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[0])
            ponto2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[1])
            nome3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[0])
            ponto3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[1])
            nome4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[0])
            ponto4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[1])
            nome5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[0])
            ponto5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[1])
            nome6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[0])
            ponto6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[1])
            nome7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[0])
            ponto7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[1])
            nome8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[0])
            ponto8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[1])
            nome9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[0])
            ponto9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[1])
            nome10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[0])
            ponto10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[1])
            nome11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[0])
            ponto11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[1])
            nome12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[0])
            ponto12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[1])
            nome13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[0])
            ponto13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[1])
            nome14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[0])
            ponto14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[1])
            nome15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[0])
            ponto15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[1])

            EmbedPu = discord.Embed(title="PlayerUnknown's Battlegrounds\n"
                                          "Servers SA | TPP | Season 9\n"
                                          "\n"
                                          "Melhores 15 Jogadores Duo:")

            EmbedPu.add_field(name="Nickname", value="__1. {}__\n"
                                                     "2. {}\n"
                                                     "3. {}\n"
                                                     "4. {}\n"
                                                     "5. {}\n"
                                                     "6. {}\n"
                                                     "7. {}\n"
                                                     "8. {}\n"
                                                     "9. {}\n"
                                                     "10. {}\n"
                                                     "11. {}\n"
                                                     "12. {}\n"
                                                     "13. {}\n"
                                                     "14. {}\n"
                                                     "15. {}\n".format(nome1, nome2, nome3, nome4, nome5,
                                                                       nome6, nome7, nome8, nome9, nome10,
                                                                       nome11, nome12, nome13, nome14, nome15), inline=True)
            EmbedPu.add_field(name="Pontos", value="__{}__\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n".format(ponto1, ponto2, ponto3, ponto4, ponto5, ponto6, ponto7,
                                                                 ponto8, ponto9, ponto10, ponto11, ponto12, ponto13,
                                                                 ponto14, ponto15), inline=True)

            EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
            EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')

            await client.send_message(message.channel, embed=EmbedPu)

            cnx.commit()
            cursor.close()
            cnx.close()

        else:

            await client.send_message(message.channel, "Executar este comando no canal #rank! Obrigado!")

    if message.content.lower().startswith('!pubrank squad'):

        if "rank" in message.channel.name:

            cnx = mysql.connector.connect(user='USER', database='DATABASE', port='3306', host='IP',
                                      password='PASSWORD')

            cursor = cnx.cursor()

            query = ("SELECT pubg_name, squad_points FROM pubgdiscord ORDER BY squad_points DESC limit 15")

            cursor.execute(query)
            starting_index = cursor.fetchall()
            starting_index_1 = str(starting_index[0])
            starting_index_2 = str(starting_index[1])
            starting_index_3 = str(starting_index[2])
            starting_index_4 = str(starting_index[3])
            starting_index_5 = str(starting_index[4])
            starting_index_6 = str(starting_index[5])
            starting_index_7 = str(starting_index[6])
            starting_index_8 = str(starting_index[7])
            starting_index_9 = str(starting_index[8])
            starting_index_dez = str(starting_index[9])
            starting_index_11 = str(starting_index[10])
            starting_index_12 = str(starting_index[11])
            starting_index_13 = str(starting_index[12])
            starting_index_14 = str(starting_index[13])
            starting_index_15 = str(starting_index[14])

            nome1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[0])
            ponto1 = re.sub('[^A-Za-z0-9]+', '', starting_index_1.split(",")[1])
            nome2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[0])
            ponto2 = re.sub('[^A-Za-z0-9]+', '', starting_index_2.split(",")[1])
            nome3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[0])
            ponto3 = re.sub('[^A-Za-z0-9]+', '', starting_index_3.split(",")[1])
            nome4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[0])
            ponto4 = re.sub('[^A-Za-z0-9]+', '', starting_index_4.split(",")[1])
            nome5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[0])
            ponto5 = re.sub('[^A-Za-z0-9]+', '', starting_index_5.split(",")[1])
            nome6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[0])
            ponto6 = re.sub('[^A-Za-z0-9]+', '', starting_index_6.split(",")[1])
            nome7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[0])
            ponto7 = re.sub('[^A-Za-z0-9]+', '', starting_index_7.split(",")[1])
            nome8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[0])
            ponto8 = re.sub('[^A-Za-z0-9]+', '', starting_index_8.split(",")[1])
            nome9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[0])
            ponto9 = re.sub('[^A-Za-z0-9]+', '', starting_index_9.split(",")[1])
            nome10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[0])
            ponto10 = re.sub('[^A-Za-z0-9]+', '', starting_index_dez.split(",")[1])
            nome11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[0])
            ponto11 = re.sub('[^A-Za-z0-9]+', '', starting_index_11.split(",")[1])
            nome12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[0])
            ponto12 = re.sub('[^A-Za-z0-9]+', '', starting_index_12.split(",")[1])
            nome13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[0])
            ponto13 = re.sub('[^A-Za-z0-9]+', '', starting_index_13.split(",")[1])
            nome14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[0])
            ponto14 = re.sub('[^A-Za-z0-9]+', '', starting_index_14.split(",")[1])
            nome15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[0])
            ponto15 = re.sub('[^A-Za-z0-9]+', '', starting_index_15.split(",")[1])

            EmbedPu = discord.Embed(title="PlayerUnknown's Battlegrounds\n"
                                          "Servers SA | TPP | Season 9\n"
                                          "\n"
                                          "Melhores 15 Jogadores Squad:")

            EmbedPu.add_field(name="Nickname", value="__1. {}__\n"
                                                     "2. {}\n"
                                                     "3. {}\n"
                                                     "4. {}\n"
                                                     "5. {}\n"
                                                     "6. {}\n"
                                                     "7. {}\n"
                                                     "8. {}\n"
                                                     "9. {}\n"
                                                     "10. {}\n"
                                                     "11. {}\n"
                                                     "12. {}\n"
                                                     "13. {}\n"
                                                     "14. {}\n"
                                                     "15. {}\n".format(nome1, nome2, nome3, nome4, nome5,
                                                                       nome6, nome7, nome8, nome9, nome10,
                                                                       nome11, nome12, nome13, nome14, nome15), inline=True)
            EmbedPu.add_field(name="Pontos", value="__{}__\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n"
                                                   "{}\n".format(ponto1, ponto2, ponto3, ponto4, ponto5, ponto6, ponto7,
                                                                 ponto8, ponto9, ponto10, ponto11, ponto12, ponto13,
                                                                 ponto14, ponto15), inline=True)

            EmbedPu.set_footer(text='Developed by: Jacques Jacob | Integrado com API Oficial PUBG®')
            EmbedPu.set_thumbnail(url='https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg')

            await client.send_message(message.channel, embed=EmbedPu)

            cnx.commit()
            cursor.close()
            cnx.close()

        else:

            await client.send_message(message.channel, "Executar este comando no canal #rank! Obrigado!")

client.run('DISCORD_TOKEN')
