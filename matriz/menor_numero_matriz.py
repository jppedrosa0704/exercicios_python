'''8) Menor número
Leia uma matriz 3x3 e mostre o menor número da matriz.
'''

def menor_numero(m):
    lista = []
    menor = m[0][0]
    for linha in m:
        for numero in linha:
            if numero < menor:
                menor = numero
    #         lista.append(numero)
    # return min(lista)
    return menor

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(menor_numero(matriz))