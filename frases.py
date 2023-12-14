arquivoTxt = "BD.txt"
def frases():
    resultados = []
    with open(arquivoTxt, "r") as arquivo:
        for linha in arquivo:
            numero, frase = linha.strip().split(",")
            resultados.append((numero, frase))
    return resultados
                       
        
def quantidadeDeLinhas():
    with open(arquivoTxt, "r") as arquivo:
        for linha in arquivo:
            linhas = arquivo.readlines()
            qtd_linhas = len(linhas)
            print(1 + qtd_linhas)
    return qtd_linhas
       
