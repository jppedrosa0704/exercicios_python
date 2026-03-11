import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adivinhar():
    '''Exercício 3: Adivinhe o Número Crie um programa que escolha
    um número secreto (você pode definir na variável)
    e peça para o usuário adivinhar. O programa deve continuar pedindo até o usuário acertar.'''
    
    num = random.randint(1, 101)
    
    while True:
        limpar_tela()
        opc = int(input('Digite um número: '))

        if opc > num:
            print('é menor.')
            input('carregue enter para para continuar...')

        elif opc < num:
            print('É maior.')
            input('carregue enter para para continuar...')
        
        else:
            print(f'{opc} é o numero da sorte. Parabéns.')
            break


adivinhar()