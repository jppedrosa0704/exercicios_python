def soma_linhas(A, x):
    for linha in A:
        if sum(linha) != x:
            return False
    return True


print(soma_linhas([[1,1],[1,1]], 2))   # True
print(soma_linhas([[1,2],[3,4]], 3))   # False
print(soma_linhas([[2,0],[1,1]], 2))