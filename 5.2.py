#TODO: medeia geometrica
lista = [1,2,3,4,5,6,7,8,9]

def media_geom(lista):
    n = len(lista)
    mult = 1

    for x in lista:
        mult *= x
    return round(mult ** (1/n), 2)

print(media_geom(lista))