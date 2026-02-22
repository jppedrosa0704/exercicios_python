lista = [1,2,3,4,5,6]
tuplo = (1,2,3,4,5,6)

for i, pos in enumerate(lista):
    print(f" na posição {i} está no valor {pos}")


for i, pos in enumerate(tuplo):
    print(f" na posição {i} está no valor {pos}")

for pos in range(len(lista)):
    print(f"Na posição {pos} tem valor {lista[pos]}")

lista = [n for n in range(10)]
print(lista)

def soma(lista):
    total = 0

    for x in lista:
        total += x
    return total
print(soma(lista))

def media(lista):
    ma = soma(lista) / len(lista)
    return ma

print(media(lista))


def mult(lista):
    total = 1

    for x in lista:
        total *= x
    return total

print(mult(lista))

print(max(lista))