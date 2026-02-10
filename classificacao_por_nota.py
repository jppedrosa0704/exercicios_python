def classificacao(n):
    return f'nota: {n:.1f} APROVADO!' if n >= 9.5 else f'nota: {n:.1f} REPROVADO'
                

print(classificacao(10))
print(classificacao(5))
print(classificacao(9.2))
print(classificacao(9.8))
print(classificacao(11))