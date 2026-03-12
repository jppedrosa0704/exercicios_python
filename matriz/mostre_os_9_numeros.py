'''Criar e mostrar matriz
Crie um programa que:
leia 9 números
armazene em uma matriz 3×3
mostre a matriz na tela.'''


def mostre_matriz(m):
    
    for c in range(0, 3):
        for l in range(0, 3):
            print(m[c][l], end=' ')
        print()

matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
]

for c in range(0, 3):
        for l in range(0, 3):
            matriz[c][l] = int(input(f'Digite um valor para [{c}], [{l}]: '))



mostre_matriz(matriz)