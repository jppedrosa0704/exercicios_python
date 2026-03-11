'''Exercício 5 — Soma dos pares
Peça um número ao usuário.
Use while para calcular a soma de todos os números pares de 0 até esse número.
'''

def soma_dos_pares(n):
    i = 0
    soma = 0
    lista = []
    while i < n + 1:
        if i % 2 == 0:
            soma += i
            lista.append(i)
        i += 1
    return soma, lista

num = int(input('Digite um número: '))
soma, lista = soma_dos_pares(num)

print(f'Números pares: {lista}')
print(f'soma dos números pares: {soma}')
