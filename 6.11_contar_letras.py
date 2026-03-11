'''6.11 Escreva uma função conta_letras(txt) que imprime uma tabela com
o número de ocorrências de cada letra na cadeia de caracteres txt, por ordem
alfabética. Letras maiúsculas, minúsculas e acentuadas devem ser consideradas
iguais. Exemplo:
>>> conta_letras("A luz do sol é amarela")
a : 4
d : 1
e : 2'''

import unicodedata
def contar_letras(txt):
    txt = txt.lower()
    contagem = {}

    # Remove acentos

    txt = unicodedata.normalize("NFD", txt)
    txt = ''.join(c for c in txt if unicodedata.category(c) != 'Mn')

    for letra in txt:
        if letra.isalpha():
            contagem[letra]= contagem.get(letra, 0) + 1

    
    for letra in sorted(contagem):
        print(f"{letra}: {contagem[letra]}")


contar_letras("A luz do sol é amarela")