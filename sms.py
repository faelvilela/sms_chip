import requests, time
from consulta import *

#Função principal do código
def envio(telefone, nome ):
    url = "http://192.168.0.11/default/en_US/sms_info.html?type=sms"

    data = {
        "line1": "1",
        # "smskey": "6578abd0",
        "action": "SMS",
        "telnum": telefone,
        "smscontent": nome + "a PERNAMBUCANAS esta facilitando o pagamento do seu acordo!",
        "send": "Send"
    }

    auth = ('admin', 'admin')

    response = requests.post(url, data=data, auth=auth)
    
    print('Enviei a frase (' + frase + ') para o numero '+ numero)
    print("Status Code:", response)
    #print("Response Text:", response.text)

# salva todas as variaveis do arquivo consulta na função conectar
resultados, num_linhas,df, conn = conectar()

#variaveis abaixo e para a automação do link...
# qtd = quantidadeDeLinhas()
# #[linha][posicao da linha]

contador = 0
while contador <= num_linhas:
    frase = resultados[contador][1]
    numero = resultados[contador][0]
    envio(numero, frase)
    contador+=1
    time.sleep(3)
    