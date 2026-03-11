'''6.12 Duas palavras ou frases são anagramas se, se escrevem com as mesmas
letras, usadas o mesmo número de vezes mas, eventualmente, em posições dife
rentes. Por exemplo, a frase em Latim “Quid est veritas?” (O que é a verdade?)
é um anagrama de “Est vir qui adest” (É o homem que está diante de si).
Escreva uma função anagramas(txt1,txt2) que verifique se as cadeias de
carateres txt1 e txt2 são anagramas; o resultado deve ser True ou False.
Deve considerar equivalentes as letras maiúsculas e minúsculas e ignorar todos
os caracteres que não são letras (espaços, sinais de pontuação, etc.); pode ainda
assumir que as cadeias não têm letras com acentos.'''

def anagramas(txt1,txt2):
    txt1 = ''.join(c.lower() for c in txt1 if c.isalpha())
    txt2 = ''.join(c.lower() for c in txt2 if c.isalpha())

    cont1 = {}
    cont2 = {}

    for letra in txt1:
        cont1[letra] = cont1.get(letra, 0) + 1
        cont2[letra] = cont2.get(letra, 0) + 1

    #compara os dicionários

    return cont1 == cont2


print(anagramas('Quid est veritas', 'Est vir qui adest' ))