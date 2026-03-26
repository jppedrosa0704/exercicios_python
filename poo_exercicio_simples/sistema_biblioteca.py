import json
import os
from unicodedata import normalize, category

# =========================================================
# UTILITÁRIOS
# =========================================================

# Limpa o terminal (compatível com Windows e Unix)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Normaliza texto removendo acentos e convertendo para minúsculas
# Usado principalmente para ordenação de títulos
def normalizar(texto):
    return ''.join(
        c for c in normalize('NFD', texto)  # separa caracteres e acentos
        if category(c) != 'Mn'              # remove os acentos
    ).lower()


# =========================================================
# PERSISTÊNCIA DE DADOS (JSON)
# =========================================================

# Carrega os dados do arquivo JSON
# Retorna uma lista de dicionários representando os livros
def carregar_dados(arquivo='sistema_biblioteca.json'):
    try:
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna lista vazia se não existir ou estiver inválido


# Salva os dados no arquivo JSON
def salvar_dados(livros, arquivo='sistema_biblioteca.json'):
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=2)


# =========================================================
# INTERFACE (MENU)
# =========================================================

# Exibe o menu principal
def menu():
    print('===========================')
    print('  📚  MENU BIBLIOTECA 📚')
    print('===========================')
    print('[1] Adicionar livro')
    print('[2] Listar livro')
    print('[3] Levantar livro')
    print('[4] Devolver livro')
    print('[5] Sair')


# =========================================================
# CLASSE PRINCIPAL (LIVRO)
# =========================================================

# Representa um livro dentro do sistema
class sistema_biblioteca:
    def __init__(self, titulo, autor, disponivel=False):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel  # False = disponível | True = emprestado

    # -----------------------------------------------------
    # Adiciona um novo livro ao sistema
    # -----------------------------------------------------
    def adicionar_livro(self, livros):

        # Cria estrutura em formato dicionário para salvar no JSON
        dados = {
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }

        titulo_existe = False

        # Verifica se o título já existe na lista
        for t in livros:
            if t['titulo'] == self.titulo:
                print(f'{self.titulo} já existe.')
                input('Press any key to continue')
                titulo_existe = True
                break

        # Caso não exista, adiciona o livro
        if not titulo_existe:
            livros.append(dados)

            # Ordena os livros por título (ignorando acentos)
            livros.sort(key=lambda l: normalizar(l['titulo']))

            salvar_dados(livros)  # persiste no JSON

            print(f'✅ {self.titulo} salvo com sucesso! 💾')
            input('\nPress any key to continue')

    # -----------------------------------------------------
    # Marca o livro como emprestado
    # -----------------------------------------------------
    def levantar_livro(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"\n✅  {self.titulo} levantado com sucesso!")
        else:
            print(f"\n⚠️  {self.titulo} Não se encontra disponível.")

        input('\nPress any key to continue...')

    # -----------------------------------------------------
    # Marca o livro como devolvido
    # -----------------------------------------------------
    def devolver_livro(self):
        if self.disponivel:
            self.disponivel = False
            print(f"✅  {self.titulo} devolvido com sucesso.")
        else:
            print('O livro já está disponível.')

        input('\nPress any key to continue')


# =========================================================
# FUNÇÕES DE VISUALIZAÇÃO
# =========================================================

# Lista todos os livros cadastrados
def listar_livros(livros):
    limpar_tela()

    # Verifica se existem livros
    if not livros:
        print('⚠️  Lista de livros vazia')
        input('\nPress any key to continue')
        return

    print("=-=-=" * 11)
    print('\t\t📚LIVROS DISPONÍVEIS📚')

    # Percorre e exibe todos os livros
    for livro in livros:
        print("=-=-=" * 11)
        print(
            f"Titulo = {livro['titulo'].capitalize()}"
            f"\nAutor = {livro['autor']}"
            f"\nDisponibilidade = {livro['disponivel']}"
        )

    print("=-=-=" * 11)
    input('\nPress any key to continue...')


# =========================================================
# LOOP PRINCIPAL DO SISTEMA
# =========================================================

# Carrega os dados ao iniciar o programa
livros = carregar_dados()

while True:
    limpar_tela()
    menu()

    try:
        opc = int(input('\nDigite sua opção: '))

        # Validação da opção do usuário
        if opc < 1 or opc > 5:
            print('⚠️  Opção inválida!')
            input('Press any key to continue')
            continue

    except ValueError:
        print('⚠️  Opção inválida!')
        input('Press any key to continue')
        continue

    match opc:

        # -------------------------------------------------
        # Adicionar livro
        # -------------------------------------------------
        case 1:
            while True:
                titulo = input('Titulo do livro: ').lower()

                if not titulo.strip():
                    print('⚠️  Não pode ficar vazio.')
                else:
                    break

            while True:
                autor = input('Autor: ')

                # Valida se contém apenas letras e espaços
                if autor.replace(" ", "").isalpha():
                    break
                else:
                    print('⚠️  autor inválido')
                    input('\nPress any key to continue.')

            dados = sistema_biblioteca(titulo, autor)
            dados.adicionar_livro(livros)

        # -------------------------------------------------
        # Listar livros
        # -------------------------------------------------
        case 2:
            listar_livros(livros)

        # -------------------------------------------------
        # Levantar (emprestar livro)
        # -------------------------------------------------
        case 3:
            while True:
                limpar_tela()
                print('===========================')
                print('\t📚BIBLIOTECA📚')
                print('===========================')

                # Exibe lista numerada
                for i, livro in enumerate(livros, start=1):
                    print(f"{i}. {livro['titulo']}")

                indice = int(input('\nDigite o índice do livro: '))

                # Validação do índice
                if indice < 1 or indice > len(livros):
                    print('⚠️  Opção inválida.')
                    input('\nPress any key to continue.')
                else:
                    break

            livro_escolhido = livros[indice - 1]

            # Converte dicionário para objeto
            livro_obj = sistema_biblioteca(
                livro_escolhido['titulo'],
                livro_escolhido['autor'],
                livro_escolhido['disponivel']
            )

            # Executa empréstimo
            livro_obj.levantar_livro()

            # Atualiza o estado no dicionário
            livro_escolhido['disponivel'] = livro_obj.disponivel

            salvar_dados(livros)

        # -------------------------------------------------
        # Devolver livro
        # -------------------------------------------------
        case 4:
            while True:
                limpar_tela()
                print('===========================')
                print('\t📚BIBLIOTECA📚')
                print('===========================')

                for i, livro in enumerate(livros, start=1):
                    print(f"{i}. {livro['titulo']}")

                indice = int(input('\nDigite o índice do livro: '))

                # Validação do índice
                if indice < 1 or indice > len(livros):
                    print('⚠️  Opção inválida.')
                    input('\nPress any key to continue.')
                else:
                    break

            livro_escolhido = livros[indice - 1]

            # Converte dicionário para objeto
            livro_obj = sistema_biblioteca(
                livro_escolhido['titulo'],
                livro_escolhido['autor'],
                livro_escolhido['disponivel']
            )

            # Executa devolução
            livro_obj.devolver_livro()

            # Atualiza estado no dicionário
            livro_escolhido['disponivel'] = livro_obj.disponivel

            salvar_dados(livros)

        # -------------------------------------------------
        # Encerrar sistema
        # -------------------------------------------------
        case 5:
            break