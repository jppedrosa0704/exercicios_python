'''5) Diagonal principal
Leia uma matriz 3x3 e mostre apenas os números da diagonal principal.

'''

def soma_diagonal_principal(m):
    
    n = len(m)
    soma = 0
    for c in range(n):
        soma += m[c][c]

    return soma

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


resultado = (soma_diagonal_principal(matriz))
print(resultado)