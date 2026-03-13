'''7) Maior número
Leia uma matriz 3x3 e mostre o maior número da matriz.
'''

def maior_numero(m):
    #numeros = [] 
    maior = [0][0]
    for c in m:
        for numero in c:
            if numero > maior:
                maior = numero
    #         numeros.append(numero)
    # return max(numeros)
    return maior
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(maior_numero(matriz))