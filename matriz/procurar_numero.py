'''9) Procurar número
Leia uma matriz 3x3 e depois peça um número ao usuário. O programa deve dizer se o número existe na matriz ou não.
'''

def procurar_numero(m):
    usuario = int(input('Digite o numero: '))
    
    for linha in m:
        for numero in linha:
            if numero == usuario:
                return True
    return False
    
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(procurar_numero(matriz))