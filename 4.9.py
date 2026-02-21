#todo: definir palavra forte pass

def rem_vogais(txt):
    vogais = 'AEIOUaeiou'
    letras = ''

    for x in txt:
        if x not in vogais:
            letras += x
    return letras

print(rem_vogais('Abracadabra!'))