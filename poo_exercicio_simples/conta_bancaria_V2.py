import json  # Biblioteca para trabalhar com arquivos JSON
import os    # Biblioteca para interagir com o sistema operacional

# Função para limpar o terminal (Windows ou Linux/Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para carregar os dados do arquivo JSON
def carregar_dados(arquivo='conta_bancaria_V2'):
    try:
        # Abre o arquivo em modo leitura
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)  # Converte JSON para lista/dicionário
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna lista vazia se não existir ou estiver corrompido
    
# Função para salvar os dados no arquivo JSON
def salvar(conta, arquivo='conta_bancaria_V2'):
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        # Salva a lista de contas no arquivo formatado
        json.dump(conta, arquivo, ensure_ascii=False, indent=2)


# Classe que representa uma conta bancária
class conta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular  # Nome do titular
        self.saldo = saldo      # Saldo inicial
    
    # Método para adicionar uma nova conta
    def adicionar_conta(self):
        limpar_tela()

        nome_existe = False
        # Verifica se o titular já existe
        for nome in conta:
            if nome['titular'] == self.titular:
                print(f'{self.titular} já cadastrado')
                nome_existe = True
                input('Press any key to continue.')
                return
            
        # Se não existir, adiciona a nova conta
        if not nome_existe:
            dados = {'titular': self.titular, 'saldo': self.saldo}
            conta.append(dados)     # Adiciona na lista
            salvar(conta)           # Salva no arquivo
            nome_existe = False
            input('Press any key to continue.')

    # Método para realizar depósito
    def depositar(self, valor):
        limpar_tela()

        # Procura a conta do titular
        for c in conta:
            if c['titular'] == self.titular:
                self.saldo += valor         # Atualiza saldo da instância
                c['saldo'] = self.saldo     # Atualiza no dicionário
                salvar(conta)               # Salva no arquivo
                print(f'Depósito de {valor:.2f} realizado com sucesso!')
                input('Press any key to continue.')
                return

    # Método para realizar saque
    def saque(self, valor):
        limpar_tela()

        # Percorre as contas
        for c in conta:
            # Verifica se há saldo suficiente
            if valor > c['saldo']:
                print('⚠️  Saldo insuficiente.')
                print(f'Saldo em conta disponível {valor:.2f}€ ')
                input('\nPress any key to continue.')
                return
            else:
                # Se o titular corresponder, faz o saque
                if c['titular'] == self.titular:
                    self.saldo -= valor
                    c['saldo'] = self.saldo
                    salvar(conta)
                    print(f'Saque de {valor:.2f}£ realizado com sucesso!')
                    input('Press any key to continue.')
                    return
            
    # Método de login do usuário
    def login(self):
        limpar_tela()

        conta_encontrada = False
        # Procura a conta pelo titular
        for c in conta:
            if c['titular'] == self.titular:
                conta_encontrada = c
                break

        # Caso não encontre a conta
        if not conta_encontrada:
            print('⚠️ Não existe conta cadastrada.')
            input('Press any key to continue.')
            return
        
        # Atualiza o saldo da instância com o saldo salvo
        self.saldo = conta_encontrada['saldo']
        
        # Loop do menu interno após login
        while True:
            limpar_tela()
            print('==========================================')
            print(f'Bem-vindo(a), {self.titular}! Saldo atual: {self.saldo:.2f}€')
            print('==========================================')
            print('[1]Depositar')
            print('[2]sacar')
            print('[3]sair')
                
            try:
                opc = int(input('escolha a opção desejada: '))
                # Validação de opção
                if opc < 1 or opc > 3:
                    print('⚠️  opção inválida')
                    input('Press any key to continue.')
                    continue
            except ValueError:
                print('⚠️  opção inválida')
                input('Press any key to continue.')
                continue

            # Estrutura match-case (tipo switch)
            match opc:
                case 1:
                    valor = float(input('Digite o valor do depósito: '))
                    self.depositar(valor)
                    continue
                case 2:
                    valor = float(input('Digite o valor do saque: '))
                    self.saque(valor)
                case 3:
                    break
        

# 💻 PROGRAMA PRINCIPAL 💻

conta = carregar_dados()  # Carrega os dados das contas

# Loop principal do sistema
while True:
    limpar_tela()
    print('===========================')
    print('  MENU DO BANCO DOS LISOS')
    print('===========================')
    print('[1] Login')
    print('[2] Cadastrar conta')
    print('[3] Sair')
    print('===========================')

    try:
        opc = int(input('Escolha a opção desejada: '))
        # Validação da opção
        if opc < 1 or opc > 3:
            print('⚠️  opção inválida.')
            input('Press any key to continue.')
            continue
    except ValueError:
        print('⚠️  opção inválida.')
        continue

    # Menu principal
    match opc:
        case 1:
            titular = input('Digite o nome do usuário: ')
            login = conta_bancaria(titular)
            login.login()
        case 2:
            titular = input('nome: ')
            nova_conta = conta_bancaria(titular)
            nova_conta.adicionar_conta()
        case 3:
            break

# Mostra todas as contas ao final do programa
print(conta)