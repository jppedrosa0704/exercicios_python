#  TODO:5.9 Escreva uma função palavras(txt) que retorna a lista das palavras na
# cadeia de caracteres txt. As palavras devem incluir apenas letras maiúsculas
# ou minúsculas; assuma ainda que a cadeia não tem letras acentuadas. Exemplo:
# >>> palavras("---A Maria tinha um cordeirinho?")
#[’A’, ’Maria’, ’tinha’, ’um’, ’cordeirinho’]

def apenas_palavras(txt):
    palavra_atual = ''
    nova_lista = []
    for l in txt:
        if l.isalpha():
            palavra_atual += l
        else:
            if palavra_atual != '':
                nova_lista.append(palavra_atual)
                palavra_atual = ''
    if palavra_atual != '':
        nova_lista.append(palavra_atual)
    return nova_lista

palavra = '---A Maria tinha um cordeirinho?'

print(apenas_palavras(palavra))


# import re

# def palavras(txt):
#     return re.findall(r'[A-Za-z]+', txt)

# palavra = '---A Maria tinha um cordeirinho?'
# print(palavras(palavra))
