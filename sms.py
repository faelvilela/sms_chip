import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import requests
from consulta import conectar
import time
import random

<<<<<<< HEAD
#Inicia uma classe para a interface e concatena as informações com as outras funções
class SMSApp:
    def __init__(self, root):
        
        #Titulo da interface
        root.config(bg='#3498db')
        self.root = root
        self.root.title("Envio de SMS")
        
        #Input para inserir o número do lote
        self.label_lote = tk.Label(root, text="Número do Lote:", bg='#87CEEB')
        self.label_lote.pack(pady=10)

        #Parametros da interface(tamanho)
        self.entry_lote = tk.Entry(root)
        self.entry_lote.pack(pady=10)
=======

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
>>>>>>> dc94e7af89d8ea6566b57bbacfda20e2f39e977d

        #Parametros do botão(Referencia para iniciar a função e tamanho)
        self.start_button = tk.Button(root, text="Iniciar Envio", command=self.ConfirmaInicio)
        self.start_button.pack(pady=10)
        
        # Adiciona a barra de progresso
        self.progress_label = tk.Label(root, text="", bg='#87CEEB')
        self.progress_label.pack(pady=10)
        

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg='#87CEEB')
        self.result_label.pack(pady=10)

    #Função que solicita um alert para confirmar o inicio do envio dos SMS
    def ConfirmaInicio(self):
        numero_lote = self.entry_lote.get()

        #Solicita o número do lote
        if not numero_lote:
            messagebox.showerror("Erro", "Por favor, insira o número do lote.")
            return

        #chama a função consulta
        telefones, nomes, num_linhas = conectar(numero_lote)

        #Caso o número do lote não seja reconhecido ele para o código
        if num_linhas == 0:
            messagebox.showinfo("Informação", "Nenhum dado encontrado para o número do lote fornecido.")
            return

        # Exibe o número de linhas na caixa de diálogo
        messagebox.showinfo("Informação", f"A consulta retornou {num_linhas} linhas. Iniciando os envios.")

        self.result_label.config(text=f"Resultado da consulta:\n{num_linhas} linhas")

        # Solicita confirmação para iniciar os envios
        confirm = messagebox.askyesno("Confirmação", "Deseja iniciar os envios de SMS?")
        
        if confirm:
            self.IniciarSMS()
    
<<<<<<< HEAD
            
    #Função para receber o número do lote e iniciar os envios
    def IniciarSMS(self):
        numero_lote = self.entry_lote.get()

        if not numero_lote:
            messagebox.showerror("Erro", "Por favor, insira o número do lote.")
            return

        #Parâmetros para chamar a função da consulta
        telefones, nomes, num_linhas = conectar(numero_lote)

        self.contador = 0
        self.total = num_linhas
        self.AtualizaOProgresso()
        self.progress_bar["maximum"] = num_linhas
        self.enviarSms(telefones, nomes, num_linhas)
        
    #Função que concatena a função de envio e a função da interface
    def enviarSms(self, telefones, nomes, num_linhas):
        if self.contador < num_linhas:
            nome = nomes[self.contador]
            telefone = telefones[self.contador]
            self.envio(telefone, nome)
            self.contador += 1
            self.progress_bar["value"] = self.contador
            self.AtualizaOProgresso()
            self.root.after(15000, self.enviarSms, telefones, nomes, num_linhas)
        else:
            messagebox.showinfo("Envio Concluído", "Todos os SMS foram enviados com sucesso!")
            
            
    #Função que realiza o request e fica responsavel por enviar os parametros para a mensagem 
    def envio(self, numero, nome):
        
        #array de frases para serem selecionadas aleatoriamente no envio
        frases = [
            "Prezado (a), pague R$50 reais HOJE no parcelamento simplificado Pernambucanas e coloque seu cartão em dia. Ligue 0806061419 ou Wtpp 1135125911."
        ]

        url = "http://192.168.0.11/default/en_US/sms_info.html?type=sms"

        data = {
            f"line{1 + (self.contador % 1)}": "1",
            "action": "SMS",
            "telnum": numero,
            "smscontent": random.choice(frases),
            "send": "Send"
        }

        auth = ('admin', 'admin')

        response = requests.post(url, data=data, auth=auth)

        print('Enviei para o numero: ' + numero)
        print("Status Code:", response)
        print(self.contador)

    #Atualiza o progresso de acordo com o contador
    def AtualizaOProgresso(self):
        progress_text = f"Progresso: {self.contador}/{self.total}"
        self.progress_label.config(text=progress_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SMSApp(root)
    root.mainloop()
=======
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
>>>>>>> dc94e7af89d8ea6566b57bbacfda20e2f39e977d
