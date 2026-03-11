def quadrado_magico(matriz, x):
    
    #Soma das linhas
    for i in matriz:
        if sum(i) != x:
            return False
    
    n = len(matriz)
    
    #Soma das colunas
    for coluna in range(n):
        soma = 0
        for linha in range(n):
            soma += matriz[linha][coluna]
        if soma != x:
            return False

    #soma da diagonal principal
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    if soma != x:
        return False
        
    #soma da diagonal secundária
    soma = 0
    for i in range(n):
        soma += matriz[i][n -1 -i]
    if soma != x:
        return False

    return True


matriz = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

print(quadrado_magico(matriz, 15))
print(quadrado_magico(matriz, 2))
