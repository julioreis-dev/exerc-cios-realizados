import requests
import json
import datetime
import time

x=True
while x:
    requ = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacao = json.loads(requ.text)
    coin = ['USD', 'USDT', 'EUR', 'CAD', 'GBP', 'ARS', 'BTC', 'LTC', 'JPY', 'CHF', 'AUD', 'ETH']
    for n in coin:
        #Configuração de datas e horários
        dia_hoje=datetime.datetime.now()
        dia=dia_hoje.strftime('%d/%m/%Y %H:%M:%S')

        # Filtragem no site das informações necessárias
        moeda = (cotacao[n]['name'])
        valor_compra = (cotacao[n]['high'])
        valor_venda = (cotacao[n]['low'])
        variacao = float(cotacao[n]['varBid'])
        print('Cotação de {}'.format(moeda))
        print('')
        print('valor de compra:', valor_compra)
        print('Valor de venda:', valor_venda)
        print('Variação do {} é: {}'.format(moeda, variacao))
        print('')
        print('########', dia,'########')
        time.sleep(5)
    x=False
print('Relatório de cotação de moedas terminado com sucesso!!!')


# temporarizacao = Timer(2, cotar)
# temporarizacao.start()
