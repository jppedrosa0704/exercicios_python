# ✅ Exercício 6 — Classificar alunos pela nota

# Crie uma função que receba uma lista de notas e retorne uma lista com:

# "Reprovado" para notas < 5

# "Recuperação" para notas de 5 a 6

# "Aprovado" para notas >= 7

# Exemplo:

# Entrada: [4, 5, 8]
# Saída: ['Reprovado', 'Recuperação', 'Aprovado']

notas = [4, 5, 8]
situacao = []
def classificar_alunos():
    for n in notas:
        if n < 5:
            situacao.append('Reprovado')
        elif n >= 5 and n < 7:
            situacao.append('Recuperação')
        else:
            situacao.append('Aprovado')

classificar_alunos()
print(situacao)