# ✅ Exercício 8 — Somar apenas números pares da lista

# Crie uma função que receba uma lista e retorne a soma somente dos números pares.

# Exemplo:

# Entrada: [1, 2, 4, 7]
# Saída: 6

numeros = [1, 2, 4, 7]
numeros_pares = []

def somar_numeros_pares():
    tot_par = 0
    for soma_par in numeros:
        if soma_par % 2 == 0:
            numeros_pares.append(soma_par)
            tot_par += soma_par
    return tot_par

resultado = somar_numeros_pares()
print(f'lista de números pares: {numeros_pares}')
print(f'Quantidade de números pares: {resultado}')


