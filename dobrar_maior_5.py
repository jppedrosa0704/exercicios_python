# Exercício 4 — Dobrar números maiores que 5

# Crie uma função que receba uma lista e retorne outra lista com os números dobrados,
# mas somente os que forem maiores que 5.

# Exemplo:

# Entrada: [2, 6, 10, 3]
# Saída esperada: [12, 20]

numeros = [2, 6, 10, 3] #entrada
dobrar_maior_5 = [] #saida

def numeros_dobrados_maior_5():
    for number in numeros:
        if number > 5: #números maiores que 5
            dobro = number * 2 #será dobrado núemeros maiores que 5
            dobrar_maior_5.append(dobro) #recebenum eros dobrados maiores que 5

numeros_dobrados_maior_5()
print(dobrar_maior_5)