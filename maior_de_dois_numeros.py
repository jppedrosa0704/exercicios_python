#Exercício 2 – Maior de dois números

#Escreva uma função maior(a, b) que devolve o maior valor usando ternário.'



def maior(a, b):
    return f'{a} é maior que {b}' if a > b else f'{b} é maior que {a}'


print(maior(5, 4))
print(maior(2, 4))
print(maior(1, 4))
print(maior(10, 4))



