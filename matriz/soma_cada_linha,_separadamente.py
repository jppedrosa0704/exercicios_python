'''3) Soma de cada linha
Leia uma matriz 3x3 e mostre a soma de cada linha separadamente.'''

def soma_linha_separadamente(m):
    soma_linhas = []
    for c in m:
        total = sum(c)
        soma_linhas.append(total)
        
    for i, c in enumerate(soma_linhas, start=1):
        print(f'soma da {i}ª linha: {c}')

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma_linha_separadamente(matriz)