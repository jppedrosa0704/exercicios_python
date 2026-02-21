# TODO: desvio Padrão
lista = [1,2,3,4,5,6,7,8,9]
from math import sqrt
def media_arit(xs):
    return sum(xs) / len(xs)

def desvio_padrão(xs):
    n = len(xs)
    media = media_arit(xs)

    soma = 0
    for xi in xs:
        soma += (xi - media) **2
    return round(sqrt(soma / (n - 1)), 2)

print('média padrão é:', desvio_padrão(lista))