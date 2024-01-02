import tkinter as tk
from tkinter import ttk, messagebox
import requests
from consulta import conectar
import time

#Inicia uma classe para a interface e concatena as informações com as outras funções
class SMSApp:
    def __init__(self, root):
        
        root.config(bg='#3498db')
        #Titulo da interface
        self.root = root
        self.root.title("Envio de SMS")

        #Input para inserir o número do lote
        self.label_lote = tk.Label(root, text="Número do Lote:", bg='#87CEEB')
        self.label_lote.pack(pady=10)
        
        #Parametros da interface(tamanho)
        self.entry_lote = tk.Entry(root)
        self.entry_lote.pack(pady=10)
        
        #Parametros do botão(Referencia para iniciar a função e tamanho)
        self.start_button = tk.Button(root, text="Iniciar Envio", command=self.start_sms_send)
        self.start_button.pack(pady=10)

        # Adiciona a barra de progresso
        self.progress_label = tk.Label(root, text="", bg='#87CEEB')
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)
        

    #Função para receber o número do lote e iniciar os envios
    def start_sms_send(self):
        numero_lote = self.entry_lote.get()

        if not numero_lote:
            messagebox.showerror("Erro", "Por favor, insira o número do lote.")
            return

        #Parâmetros para chamar a função da consulta
        telefones, nomes, num_linhas = conectar(numero_lote)

        if num_linhas == 0:
            messagebox.showinfo("Informação", "Nenhum dado encontrado para o número do lote fornecido.")
            return

        self.contador = 0
        self.total = num_linhas
        self.AtualizaOProgresso()
        self.progress_bar["maximum"] = num_linhas
        self.enviar_sms(telefones, nomes, num_linhas)

    #Função que concatena a função de envio e a função da interface
    def enviar_sms(self, telefones, nomes, num_linhas):
        if self.contador < num_linhas:
            nome = nomes[self.contador]
            telefone = telefones[self.contador]
            self.envio(telefone, nome)
            self.contador += 1
            self.progress_bar["value"] = self.contador
            self.AtualizaOProgresso()
            self.root.after(15000, self.enviar_sms, telefones, nomes, num_linhas)
        else:
            messagebox.showinfo("Envio Concluído", "Todos os SMS foram enviados com sucesso!")
            
            
    #Função que realiza o request e fica responsavel por enviar os parametros para a mensagem 
    def envio(self, numero, nome):
        url = "http://192.168.0.11/default/en_US/sms_info.html?type=sms"

        data = {
            f"line{1 + (self.contador % 5)}": "1",
            "action": "SMS",
            "telnum": numero,
            "smscontent": "Prezado(a), regularize com 90% de desconto seu débito com a Caixa e regularize seu CPF em 48horas . Ligue agora para 0806066356 ou wtpp 1135125911.",
            "send": "Send"
        }

        auth = ('admin', 'admin')

        response = requests.post(url, data=data, auth=auth)

        print('Enviei para o numero: ' + numero)
        print("Status Code:", response)

    #Atualiza o progresso de acordo com o contador
    def AtualizaOProgresso(self):
        progress_text = f"Progresso: {self.contador}/{self.total}"
        self.progress_label.config(text=progress_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SMSApp(root)
    root.mainloop()

