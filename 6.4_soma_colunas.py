'''6.4 Escreva uma função soma_colunas(A,x) que, dada uma matriz A de n×n
de números inteiros (representada como lista de listas), verifica se a soma dos
valores por coluna é igual a x. O resultado deverá ser True no caso de todas as
colunas da matriz terem soma igual a x e False, caso contrário.'''

def soma_colunas(xs, x):

    n = len(xs)

    for coluna in range(n):
        soma = 0
        for linha in range(n):
            soma += xs[linha][coluna]
        
        if soma != x:
            return False
    return True


matriz = [
    [3, 2, 5],
    [2, 7, 4],
    [5, 1, 1]
]

print(soma_colunas(matriz, 10))