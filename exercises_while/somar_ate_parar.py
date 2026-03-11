''' Exercício 2 — Soma até parar
    Peça números ao usuário continuamente.
    Quando o usuário digitar 0, o programa deve parar.
    No final mostre a soma total dos números digitados.

    Espaço para resposta:'''

soma = 0
while True:
    try:
        numero = int(input('Digite um número: '))
        if numero == 0:
            break
    except ValueError:
        print('Digite apenas números')
        
    soma += numero

print(f'A soma dos números foi: {soma}')
