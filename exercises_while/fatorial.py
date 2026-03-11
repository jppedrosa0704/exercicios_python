'''Exercício 6 — Fatorial
Peça um número inteiro positivo.
Use while para calcular o fatorial desse número.
'''

def fatorial(n):
    mult = 1
    while n > 0 :
        mult *= n
        n -= 1
    return mult

num = int(input('Digite um número: '))
print(fatorial(num))
