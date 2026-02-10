# Exercício 6 – Lista transformada com ternário

# Dada uma lista de números, criar outra lista que diga “P” ou “I”.

nums = [3, 6, 7, 10]

resultado = ['p' if n % 2 == 0 else 'i' for n in nums]
print(resultado)