'''2.15 Num triângulo cada lado tem um comprimento menor que a soma dos
comprimentos dos outros dois e maior que a sua diferença absoluta. Escreva
uma função triangulo(a,b,c) que verifica esta condição sobre os lados a,b,c;
o resultado deve ser True ou False'''


def triangulo(a,b,c):
    return a < b + c and b < a + c and c < a + b



print(triangulo(12, 5, 8))
print(triangulo(2, 5, 8))
print(triangulo(3, 7, 8))
print(triangulo(12, 6, 3))