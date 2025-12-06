# Crie uma função que receba uma lista de temperaturas e retorne uma nova lista dizendo para cada valor:

# "Frio" se < 15

# "Agradável" se entre 15 e 25

# "Quente" se > 25

# Exemplo:

# Entrada:
# [10, 18, 30]
# Saída esperada:
# ["Frio", "Agradável", "Quente"]

temperatura = [10, 18, 30] #celsius
situacao = []
def classificar_temperatura(temp):

    for r in temp:
        if r <= 10:
            situacao.append('Frio')
        elif r > 10 and r <= 18:
            situacao.append('Agradavel')
        else:
            situacao.append("Quente")


classificar_temperatura(temperatura)
print(situacao)