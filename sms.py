import requests, time
from consulta import *


#Função principal do código
def envio(numero, nome):
    url = "http://192.168.0.11/default/en_US/sms_info.html?type=sms"

    data = {
        f"line{contador % 32 or 32}": "1",
        # "smskey": "6578abd0",
        "action": "SMS",
        "telnum": numero,
        "smscontent": "Prezado(a), use o 13º para programar o pgto do seu cartao ELO Pernambucanas. Desconto de ate 90% pra quem retornar HOJE no 08006061419 ou WhatsApp 11 35125911",
        "send": "Send"
    }

    auth = ('admin', 'admin')

    response = requests.post(url, data=data, auth=auth)
    
    print('Enviei para o numero: '+ numero)
    print("Status Code:", response)
    #print("Response Text:", response.text)



def main():
    telefones, nomes, num_linhas = conectar()
    global contador
    contador = 0
    while contador <= num_linhas:
        nome = nomes[contador]
        telefone = telefones[contador]
        envio(telefone, nome)
        contador+=1
        print(contador)
        time.sleep(10)


main()

# contador = 0
# envio('+5531989293584', 'Rafael')
# time.sleep(10)
# envio('+5531975634365', 'Vesley')
# time.sleep(10)
# envio('+5531996413050', 'Arthur')
# # time.sleep(10)
# # envio('+5531983344390', 'Diego')
# # time.sleep(10)
# # envio('+5531994940257', 'Thiago')