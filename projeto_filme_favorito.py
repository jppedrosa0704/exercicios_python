#======== BIBLIOTECAS ========
import os
import json

#======== ARQUIVOS ========
def carregar_dados(arquivo="filmes.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(filmes, arquivo="filmes.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(filmes, f, ensure_ascii=False, indent=4)

# ======== UTILIDADES ========
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# ======== MENU ========
def menu():
    print("=-"*20)
    print(f'{"MENU":^40}')
    print("=-"*20)
    print('[1] adicionar filme')
    print('[2] remover filme')
    print('[3] listar filme por gênero')
    print('[4] sair')

# ======== ADICIONA FILMES E GÊNEROS
def adicionar_filmes(filmes):
    
    while True:
        titulo = input('Digite o título do filme (0 para cancelar): ').strip()
        if not titulo.strip():
            print("⚠️  Não pode conter espaços.")
            input('carregue "ENTER" para continuar...')
            continue
        
        #verifica se tem filme repetido
        duplicado = False
        for filme in filmes:
            if filme['título'].lower() == titulo.lower():
                print('Filme já existe')
                duplicado = True
                break
        if duplicado:
            return #sai da função
        
        if titulo == '0':
            return
        else:
            break
    
    while True:
        genero = input('Digite o gênero do filme (0 para cancelar): ').strip()
        if not genero.strip():
            print("⚠️  Não pode conter espaços.")
            continue
        if genero == '0':
            break
        else:
            break
    
    dados = {'título': titulo, 'gênero': genero}
    filmes.append(dados)
    salvar_dados(filmes, arquivo="filmes.json")
    print(f'💾  {titulo} salvo com sucesso!🎉')
    input('carregue "ENTER" para continuar...')
# ======== REMOVE FILMES DA LISTA
def remover_filme(filmes):
    limpar_tela()
    if not filmes:
        print('Não há filmes no catálogo ')
        input('carregue "ENTER" para continuar...')
    
    
    while True:
        limpar_tela()
        for i, fime in enumerate(filmes, start=1):
            print('=-' * 20)
            print(f"ID: {i}    Título: {fime['título']}")
        print('=-' * 20)

        try:
            remover = int(input("Digite o ID do filme (0 para sair): "))
            if remover == 0:
                print('Operação cancelada pelo usuário.')
                input('carregue "ENTER" para continuar...')
                return
            if remover < 1 or remover > len(filmes):
                print('⚠️  opção inválida!')
                input('carregue "ENTER" para continuar...')
                continue
            else:
                break
        except ValueError:
            print('⚠️  opção inválida!')
            input('carregue "ENTER" para continuar...')
            continue
    filme_removido = filmes[remover - 1 ]
    del filmes[remover - 1 ]
    print(f'{filme_removido} removido com sucesso!🎉')
    input('carregue "ENTER" para continuar...')
    salvar_dados(filmes)
    #filmes.clear() limpa a lista e deixa apenas vazio

# LISTA FILMES POR GÊNEROS
def listar_filmes(filmes):
    
    while True:
        limpar_tela()

        #Verifca os generos dos filmes e grava dentro da lista sem repetir
        generos_unicos = [] 
        for f in filmes:
            if f['gênero'] not in generos_unicos:
                generos_unicos.append(f['gênero'])

        for i, genero in enumerate(generos_unicos, start=1):
            print(f'{i}. {genero}')
        try:
            opc = int(input('Digite o código do Gênero: '))
            if opc >= 1 or opc <= len(generos_unicos):
                genero_escolhido = generos_unicos[opc - 1]
                print(f'Gênero escolhido: {genero_escolhido}')
                input('carregue "ENTER" para continuar...')
                break
            else:
                print("⚠️ Opção inválida!")
                input('carregue "ENTER" para continuar...')
                continue
        except ValueError:
            print('⚠️ Opção inválida!')
            input('carregue "ENTER" para continuar...')
            continue

    print(f"\nFilmes do gênero '{genero_escolhido}':")
    contador = 1
    for f in filmes:
        if f['gênero'] == genero_escolhido:
            print(f'{contador}. {f['título']}')
            contador += 1

    input("\nCarregue ENTER para continuar...")

limpar_tela()
filmes = carregar_dados()

#======== PROGRAMA PRINCIPAL ========
while True:
    while True:
        limpar_tela()
        menu()
        try:
            opc = int(input('escolha a opção desejada: '))
            if opc < 1 or opc > 4:
                print('⚠️ Opção inválida!')
                input('carregue "ENTER" para continuar...')
            else:
                break
        except ValueError:
            print('⚠️ Opção inválida!')
            input('carregue "ENTER" para continuar...')
            continue
    match opc:
        case 1:
            adicionar_filmes(filmes)
        case 2:
            remover_filme(filmes)
        case 3:
            listar_filmes(filmes)
        case 4:
            break

print(filmes)
