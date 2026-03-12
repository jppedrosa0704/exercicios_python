'''4) Soma de cada coluna
Leia uma matriz 3x3 e mostre a soma de cada coluna
'''

def soma_coluna(m):
    for c in range(0, 3):
        soma = 0
        for l in range(0, 3):
            soma += m[l][c]
        print(f'Soma da {c+1}ª coluna foi: {soma}')


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma_coluna(matriz)