# TODO: 5.4 Escreva uma função intervalo(xs,a,b) cujo resultado é a contagem dos
# valores da lista xs que estão entre a e b inclusivé; pode assumir que a ≤ b.


lista = [1,2,3,4,5,6,7,8,9]

def intervalos(xs, a, b):
    cont = 0
    for x in xs:
        if x >= a and x <= b:
            cont += 1
    return cont
print(intervalos(lista, 2, 8))
