import requests, time
from frases import *

def envio(numero, frase):
    url = "http://192.168.0.11/default/en_US/sms_info.html?type=sms"

    data = {
        f"line{contador % 2 or 2}": "1",
        "smskey": "6579d846",
        "action": "SMS",
        "telnum": "+55" + numero,
        "smscontent": "teste",
        "send": "Send"
    }

    auth = ('admin', 'admin')

    response = requests.post(url, data=data, auth=auth)

    print('Enviei a frase (' + frase + ') para o numero '+ numero)
    print("Status Code:", response.status_code)
    #print("Response Text:", response.text)

resultados = frases()
qtd = quantidadeDeLinhas()
#[linha][posicao da linha]

contador = 0
while contador <= qtd:
    frase = resultados[contador][1]
    numero = resultados[contador][0]
    envio(numero, frase)
    contador+=1
    time.sleep(10)
    