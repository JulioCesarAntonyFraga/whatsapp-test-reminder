import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime as dt
import time
import mysql.connector


print('Rodando...')

cnx = mysql.connector.connect(user='xxxx', password='xxxx',
                              host='xxxx',
                              database='xxxx')

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = 'xxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxx'

client = Client(account_sid, auth_token, http_client=proxy_client)

nums = ['+2222222222','+33333333333', '+444444444444', '+555555555', '+66666666666', '+55555555', '+999999999999', '+1111111111']
hora8 = True
hora12 = True
hora18 = True
hora20 = True


def msg8():

    c = cnx.cursor()
    c.execute(
        "SELECT * FROM provas"
    )

    records = c.fetchall()

    for info in records:
        if info[1] == d1:
            print('Enviando mensagem as 8 horas')
            for num in nums:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=f'AMANHÃ TEM PROVA! NÃO SE ESQUEÇA DE ESTUDAR!\n\nData:{info[1]}\nMatéria: {info[0]}\nConteúdo:{info[2]}',
                    to=f'whatsapp:{num}'
                )
    global hora8
    hora8 = False

def msg12():
    c = cnx.cursor()
    c.execute(
        "SELECT * FROM provas"
    )

    records = c.fetchall()

    for info in records:
        if info[1] == d1:
            print('Enviando mensagem as 12 horas')
            for num in nums:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=f'AMANHÃ TEM PROVA! NÃO SE ESQUEÇA DE ESTUDAR!\n\nData:{info[1]}\nMatéria: {info[0]}\nConteúdo:{info[2]}',
                    to=f'whatsapp:{num}'
                )
    global hora12
    hora12 = False

def msg18():
    c = cnx.cursor()
    c.execute(
        "SELECT * FROM provas"
    )

    records = c.fetchall()

    for info in records:
        if info[1] == d1:
            print('Enviando mensagem as 18 horas')
            for num in nums:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=f'AMANHÃ TEM PROVA! NÃO SE ESQUEÇA DE ESTUDAR!\n\nData:{info[1]}\nMatéria: {info[0]}\nConteúdo:{info[2]}',
                    to=f'whatsapp:{num}'
                )
    global hora18
    hora18 = False

def msg20():
    c = cnx.cursor()
    c.execute(
        "SELECT * FROM provas"
    )

    records = c.fetchall()

    for info in records:
        if info[1] == d1:
            print('Enviando mensagem as 20 horas')
            for num in nums:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=f'AMANHÃ TEM PROVA! NÃO SE ESQUEÇA DE ESTUDAR!\n\nData:{info[1]}\nMatéria: {info[0]}\nConteúdo:{info[2]}',
                    to=f'whatsapp:{num}'
                )
    global hora20
    hora20 = False



while True:
    time.sleep(2)
    tomorrow = dt.date.today() + dt.timedelta(days=1)
    # dd/mm/YY
    d1 = tomorrow.strftime("%d/%m/%Y")
    hora = dt.datetime.now().hour
    if hora == 11 and hora8:
        msg8()
    if hora == 15 and hora12:
        msg12()
    if hora == 21 and hora18:
        msg18()
    if hora == 23 and hora20:
        msg20()

    if hora == 0:
        hora8 = True
        hora12 = True
        hora18 = True
        hora20 = True
