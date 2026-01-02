# 💰 PROJETO – SISTEMA DE CONTROLE FINANCEIRO (INTERMEDIÁRIO)
# 🎯 Objetivo Geral

# Desenvolver um sistema em Python (terminal) que permita cadastrar usuários
# e controlar receitas e despesas, gerando relatórios financeiros.

# 🧠 Conceitos obrigatórios

# Você deve usar:

# Dicionários

# Listas

# Condições (if / elif / else)

# Loops (while / for)

# Funções

# Tratamento de erros (try / except)
import os
import json

def salvar_dados(usuarios, arquivo='usuarios.json'):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def carregar_dados(arquivo='usuarios.json'):
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_usuario(usuarios):
    while True:
        email = input("Digite o email: ")
        if '@' not in email:
            print("Email inválido.")
            continue
        
        if email in usuarios:
            print("E-mail já cadastrado")
            return
        nome = input("nome: ")
        if nome.isdigit():
            print("Não pode conter números")
            continue
        if not nome.strip():
            print("Nome não pode estar vazio.")
            continue

        usuarios[email] = {'nome': nome,
                        'movimentacoes': []
        }
        print("usuário cadastrados com sucesso.")
        salvar_dados(usuarios)
        input("\nCarregue 'ENTER' para continuar...")
        return
        
        

def registrar_receita(usuarios):

    email = input("email: ").strip()
    if email not in usuarios:
        print("email não cadastrado.")
        input("ENTER para continuar...")
        return
    
    descrição = input("Digite a decrição do movimento: ")
    if descrição.isdigit():
        print("Não pode conter números.")
        return
    
    try:
        valor = float(input("Digite o valor da despesa: "))
        if valor <= 0:
            print("O valor tem que ser menor que zero.")
            input("ENTER para continuar...")
            return
    
    except ValueError:
        print("Valor inválido.")
        input("ENTER para continuar...")
        return
    
    dados = {'tipo': 'receita', 'descrição': descrição, 'valor': valor}
    usuarios[email]['movimentacoes'].append(dados)
    salvar_dados(usuarios)
    input("ENTER para continuar...")
    return

def registrar_despesas(usuarios):
    # usuarios[email] = {'nome': nome,
        #                     'movimentacoes': []
        #     }
    email = input("email: ")
    if email not in usuarios:
        print("email não cadastrado.")
        input("ENTER para continuar...")
        return
    descrição = input("Digite a decrição do movimento: ")
    if descrição.isdigit():
        print("Não pode conter números.")
        return
    try:
        valor = float(input("Digite o valor da despesa: "))
        if valor <= 0:
            print("despesa não pode ser menor que $1.00")
            input("Carregue 'ENTER' para continuar...")
            return
    except ValueError:
        print("Valor inválido.")
        return
    
    dados = {'tipo': 'despesa', 'descrição': descrição, 'valor': valor}
    usuarios[email]['movimentacoes'].append(dados)
    salvar_dados(usuarios)
    return

def listar_movimentacoes(usuarios):
    email = input('email: ').strip()
    if email not in usuarios:
        print('e-mail não cadastrado.')
        input("Carregue 'ENTER' para continuar...")
        return
    if not usuarios[email]['movimentacoes']:
        print(f"{email} Não possui movimentações cadastradas.")
        input("carregue 'ENTER' para continuar...")
    
    else:
        print("=-" *20)
        print(f"Movimentações de {usuarios[email]['nome'].title()}")
        for i , mov in enumerate(usuarios[email]['movimentacoes'], start=1):
            print("=-" *20)
            print(f"Tipo: {mov['tipo']} \ndescrição: {mov['descrição']} \nSalário: ${mov['valor']:.2f}")
        print("=-" *20)
        input("ENTER para continuar...")

def relatorio_financeiro(usuarios):
    email = input('email: ').strip()
    if email not in usuarios:
        print('e-mail não cadastrado.')
        input("Carregue 'ENTER' para continuar...")
        return
    
    total_receitas = 0
    total_despesas = 0
    
    for mov in usuarios[email]['movimentacoes']:
        if mov['tipo'] == 'receita':
            total_receitas += mov['valor']
        elif mov['tipo'] == 'despesa':
            total_despesas += mov['valor']
    saldo = total_receitas - total_despesas

    print(f"\nRelatório financeiro de {usuarios[email]['nome'].title()}:\n")
    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo final: $ {saldo:.2f}")

    input("\nPressione ENTER para continuar...")
# usuarios = {
#     'jp@email.com': {
#         'nome': 'João Paulo',
#         'movimentacoes': [
#             {'tipo': 'receita', 'descrição': 'salário', 'valor': 2500.00}
#         ]
#     }
# }

usuarios = carregar_dados()
# limpar_tela()


while True:
    limpar_tela()
    print("[1] Cadastrar usuário")
    print("[2] Registrar receita")
    print("[3] Registrar despesa")
    print("[4] Listar movimentações")
    print("[5] Gerar relatório financeiro")
    print("[6] Sair")
    while True:
        try:
            opção = int(input("Escolha uma opção: "))
            if opção < 1 or opção > 6:
                print("⚠️  Opção inválida")
                continue
            else:
                break
        except ValueError:
            print("Opção inválida.")
        continue
        
    match opção:
        case 1:
            cadastrar_usuario(usuarios)
        case 2:
            registrar_receita(usuarios)
        case 3:
            registrar_despesas(usuarios)
        case 4:
            listar_movimentacoes(usuarios)
        case 5:
            relatorio_financeiro(usuarios)
        case 6:
            break

#print(usuarios)