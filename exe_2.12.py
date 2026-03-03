'''
2 A soma dos desvios quadrados é uma medida comum para avaliar erros.
Dada uma lista de n desvios (d1,d2,...,dn), esse valor é dado por n
i=1d2
i.
Implemente a função sdq(d), que dada uma lista de desvos d, retorna a soma
dos desvios quadrados.
'''


def sdq(xs):
    return round((xs[0]**2) + (xs[1]**2), 2)


print(sdq([-6.9, 4.7]))


