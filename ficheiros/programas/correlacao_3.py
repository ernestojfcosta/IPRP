import urllib.request
import math
import matplotlib.pyplot as plt

def media(lista):
    """ 
    Calcula a média.
    """
    med = sum(lista) / float(len(lista))
    return med

def desvio_padrao(lista):
    """
    Calcula o desvio padrão.
    """
    a_media = media(lista) 
    
    soma = 0
    for elem in lista:
        soma = soma + (elem - a_media) ** 2
    desvio = math.sqrt(float(soma) / (len(lista) - 1))
    return desvio

def pearson(lista_a, lista_b):
    """ Calcula o coeficiente de correlação de Pearson entre duas listas de valores."""
    media_a = media(lista_a)
    media_b = media(lista_b)
    
    desvio_a = desvio_padrao(lista_a)
    desvio_b = desvio_padrao(lista_b)
    n = len(lista_a) 
    soma = 0
    for indice in range(n):
        soma = soma + (lista_a[indice] - media_a) * (lista_b[indice] - media_b)
    correlacao = float(soma) / ((n - 1) * desvio_a * desvio_b)   
    return correlacao

if __name__ == '__main__':
    url_apple = urllib.request.urlopen('http://ichart.finance.yahoo.com/table.csv?s=AAPL')
    dados_apple = url_apple.readlines()[1:21]
    dados_apple_fecho = [float(str(linha[:-1],'utf-8').split(',')[4]) for linha in dados_apple]
 
    url_coke = urllib.request.urlopen('http://ichart.finance.yahoo.com/table.csv?s=Coke')
    dados_coke = url_coke.readlines()[1:21]
    dados_coke_fecho = [float(str(linha[:-1],'utf-8').split(',')[4]) for linha in dados_coke]
        
    corre = pearson(dados_apple_fecho, dados_coke_fecho)
    
    print(corre)

    
    