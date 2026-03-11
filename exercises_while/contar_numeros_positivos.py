'''Exercício 4 — Contar números positivos
    Peça números ao usuário até ele digitar 0.
    No final mostre quantos números positivos foram digitados.
'''
lista = []

def contar_numeros_positivos(n):
    i = 0
    qtd_positivos = 0
    while i < n + 1:
        if i % 2 == 0:
            qtd_positivos += 1
            lista.append(i)
        i += 1
    return qtd_positivos


num = int(input('Digite um número: '))

print(f'Quantidade de números positivos: {contar_numeros_positivos(num)}')
print(f'Números positivos: {lista}')
