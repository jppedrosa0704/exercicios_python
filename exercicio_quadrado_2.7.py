'''
2.7 Escreva uma função tabela_quadrados(n) que, para os n primeiros nú
meros inteiros positivos, imprime em cada linha o número e o seu quadrado,
separados por um espaço. Pode assumir que n > 0.
'''

def tabela_quadrados(n):
    
    for i in range(8):
        print (f'quadrado de {i} é: {i**2}')


tabela_quadrados(8)