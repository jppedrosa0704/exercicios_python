import math

def desvio_padrao(lista):
    n = len(lista)
    media = sum(lista) / n
    soma = 0

    for x in lista:
        soma += (x - media) ** 2


    return math.sqrt(soma / (n - 1))




print(round(desvio_padrao([3, 4]), 4))