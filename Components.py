from consulta import conectar
from tkinter import ttk, messagebox, simpledialog


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
  
#Atualiza o progresso de acordo com o contador      
def AtualizaOProgresso(self):
        progress_text = f"Progresso: {self.contador}/{self.total}"
        self.progress_label.config(text=progress_text)

