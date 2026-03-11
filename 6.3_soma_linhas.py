'''6.3 Escreva uma função soma_linhas(A,x) que, dada uma matriz A de n×n
de números inteiros (representada como lista de listas), verifica se a soma dos
valores por linha é igual a x. O resultado deverá ser True no caso de todas as
linhas da matriz terem soma igual a x e False, caso contrário.'''

def soma_linhas(xs, x):

    for linha in xs:
        if sum(linha) != x:
            return False
    return True

matriz = [
        [1,1,1],
        [0,2,1],
        [0,3,0]
]

print(soma_linhas(matriz, 3))
