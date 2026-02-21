# TODO: 5.7 Recorde que um número inteiro d é divisor próprio de n se e só se o resto
# da divisão de n por d for zero e d for inferior a n.
# (a) Escreva uma função divisores(n) que calcula a lista dos divisores de
# próprios de n, por ordem crescente.
# Exemplo: divisores(12) dá [1, 2, 3, 4, 6]

def divisores(n):
    divisor = [k for k in range(1, 13)]
    numeros = []

    for k in divisor:
        if n % k == 0:
            numeros.append(k)
            y = max(numeros)
            numeros_2 = [k for k in numeros if k != y]
    return numeros_2
    
    
        

    

print(divisores(12))