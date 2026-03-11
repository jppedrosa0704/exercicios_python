'''Exercício 3 — Tabuada
    Peça um número ao usuário.
    Use while para mostrar a tabuada desse número de 1 até 10.
'''

i = 0
num = int(input('Digite um número:'))
while i < 10 + 1:
    if i > 0:
        print(f'{num} x {i} = {num * i}')
    i += 1

