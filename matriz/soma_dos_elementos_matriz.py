'''2) Soma dos elementos
Leia uma matriz 3x3 e mostre a soma de todos os elementos.
'''

def mostra_matriz(m):
    for c in range(0, 3):
        for l in range(0, 3):
            print(f'{m[l][c]}', end=' ')
        print()



def soma_matriz(m):
    soma = 0
    for c in range(0 , 3):
        for l in range(0, 3):
            soma += m[l][c]
    print(f'Soma dos elementos foi: {soma}')
    
matriz = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
]

for c in range(0, 3):
    for l in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para matriz {[c]}{[l]}: '))

mostra_matriz(matriz)
soma_matriz(matriz)