'''Exercício: Conta Bancária

Crie uma classe ContaBancaria com os seguintes requisitos:

Atributos privados: titular (nome da pessoa) e _saldo (saldo da conta).
Getter (@property): saldo — deve retornar o saldo atual.
Setter (@saldo.setter): permite atualizar o saldo, mas não pode ser negativo. Se tentar, deve lançar um erro.
Método depositar(valor) — adiciona um valor ao saldo.
Método sacar(valor) — subtrai um valor do saldo, mas não pode deixar o saldo negativo.'''


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('O saldo não pode ser negativo.')
        self._saldo = valor

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado com sucesso.\n'
            f"Saldo: {self._saldo:.2f}€")

    def sacar(self, valor):
        if valor <= 0:
            print('valor do saque inválido.')
            return
        if valor > self._saldo:
            print('Não tem saldo em conta disponível')
            print(f'Saldo disponível: {self._saldo:.2f}€')
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso.\n"
                f"Novo saldo: {self.saldo:.2f}€")


c1 = ContaBancaria('João')

print('====MENU====')
print('[1] Mostrar saldo')
print('[2] Depositar')
print('[3] Sacar')
print('[4] Sair')

while True:
    try:
        opc = int(input('Escolha a opcao desejada:'))
        if opc < 1 or opc > 4:
            continue
    except ValueError:
        print('opção inválida')
        continue
    match opc:
        case 1:
            print(f'Saldo: {c1.saldo:.2f}€')
        case 2:
            valor = float(input('valor do depósito: '))
            c1.depositar(valor)
        case 3:
            valor = float(input('valor do saque: '))
            c1.sacar(valor)
        case 4:
            break
# c1.saldo = 300

print(c1.saldo)