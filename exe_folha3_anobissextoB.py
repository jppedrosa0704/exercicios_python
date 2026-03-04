'''3.6 Teste a função do exercício anterior (3.5) fazendo um programa que escreve
uma tabela dos anos bissextos entre 2000 e 2020. Verifique os resultados usando
o calendário do computador.'''

def anobissexto(a):
    for i in a:
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            print(f'{i} é Bissexto')
        else:
            print(f'{i} não é bissexto.')
    



anos = [year for year in range(2000, 2027)]

anobissexto(anos)