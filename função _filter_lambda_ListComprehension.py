lista = [2, 3 ,4, 8, 7, 9]

print('Pares com função lambda')
pares_lambda = list(filter(lambda p: p % 2 == 0, lista))
print('Lista de números pares: ')
print(pares_lambda)
print('------------------------')
print()

print('Lista de pares com list comprehension')
pares_comprehension = [l for l in lista if l % 2 == 0] #list comprehension
print(pares_comprehension)
print('------------------------')
print()
print('Ordenando a lista por idade com lambda e sort ')
dados = [
    {'nome': 'João', 'idade': 39},
    {'nome': 'Bluff', 'idade': 43},
    {'nome': 'André', 'idade': 40}
]
dados.sort(key=lambda i: i['idade']) #ordena por idade
print(*dados, sep='\n')

