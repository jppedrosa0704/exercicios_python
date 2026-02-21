# TODO: 5.7 Recorde que um número inteiro d é divisor próprio de n se e só se o resto
# da divisão de n por d for zero e d for inferior a n.
# (a) Escreva uma função divisores(n) que calcula a lista dos divisores de
# próprios de n, por ordem crescente.
# Exemplo: divisores(12) dá [1, 2, 3, 4, 6]

def divisor(n):
    numeros = []

    for d in range(1, n + 1):
        if n % d == 0:
            numeros.append(d)

    numeros.remove(max(numeros))
    return numeros

print(divisor(12)) #[1, 2, 3, 4, 6]