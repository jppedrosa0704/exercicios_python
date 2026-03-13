def soma_diagonal_inversa(m):
    n = len(m)
    soma = 0

    for di in range(len(m)):
        soma += m[di][n -1 -di]
    return soma

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


resultado = soma_diagonal_inversa(matriz)
print(resultado)
