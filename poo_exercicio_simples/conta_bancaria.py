# Exercício: Classe "ContaBancaria"

# Crie uma classe chamada ContaBancaria.

# 🔹 Atributos:
# titular (nome da pessoa)
# saldo (começa com 0)
# 🔹 Métodos:
# depositar(valor) → adiciona dinheiro ao saldo
# sacar(valor) → retira dinheiro (se houver saldo suficiente)
# mostrar_saldo() → mostra o saldo atual

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class conta_bancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0

    def adicionar(self, valor):
    
        self.saldo += valor
        print(f'saldo disponível {self.saldo:.2f}€')
        input('Press any key to exit...')
        return

    def retirar_saldo(self, valor):
        if self.saldo < valor:
            print('Não há saldo suficiente')
            print(f'saldo disponível: {self.saldo:.2f}€')
            input('Press any key to exit...')
            return
        else:
            self.saldo -= valor
            print(f'Saldo diposnível {self.saldo:.2f}€')
            input('Press any key to exit...')

    def saldo_conta(self):
        print(f'Saldo disponível: {self.saldo:.2f}€')
        input('Press any key to exit...')
        return


p1 = conta_bancaria('João Paulo')


while True:
    limpar_tela()

    print('[1] Adicionar saldo a conta')
    print('[2] Retirar saldo da conta')
    print('[3] saldo da conta')
    print('[4] sair')

    opcao = int(input('Escolha uma opção desejada: '))

    try:
        if opcao < 1 or opcao > 4:
            print('⚠️  opcao inválida')
            input('carregue enter para continuar...')
            continue
    except ValueError:
        print('⚠️  opcao inválida')
        continue

    match opcao:
        case 1:
            valor = float(input("Digite o valor para depositar: "))
            p1.adicionar(valor)
            continue
            
        case 2:
            valor = float(input('valor: '))
            p1.retirar_saldo(valor)
            continue
        case 3:
            p1.saldo_conta()
            continue
        case 4:
            break
