import json
import os
from unicodedata import normalize, category

# Limpa o terminal (Windows ou Linux/Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Remove acentos e coloca tudo em minúsculo (para ordenação)
def normalizar(texto):
    return ''.join(
        c for c in normalize('NFD', texto)  # separa letras de acentos
        if category(c) != 'Mn'              # remove os acentos
    ).lower()

# Carrega os dados do arquivo JSON
def carregar_dados(arquivo='sistema_biblioteca.json'):
    try:
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)  # retorna lista de livros (dicionários)

    except (FileNotFoundError, json.JSONDecodeError):
        return []  # se não existir ou estiver vazio, retorna lista vazia

# Salva os dados no arquivo JSON
def salvar_dados(livros, arquivo='sistema_biblioteca.json'):
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=2)

# Menu principal
def menu():
    print('===========================')
    print('  📚  MENU BIBLIOTECA 📚')
    print('===========================')
    print('[1] Adicionar livro')
    print('[2] Listar livro')
    print('[3] Levantar livro')
    print('[4] Devolver livro')
    print('[5] Sair')


# Classe que representa um livro
class sistema_biblioteca:
    def __init__(self, titulo, autor, disponivel=False):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel  # False = disponível, True = emprestado

    # Adiciona um novo livro
    def adicionar_livro(self, livros):
        dados = {
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }
        
        titulo_existe = False

        # Verifica se o livro já existe
        for t in livros:
            if t['titulo'] == self.titulo:
                print(f'{self.titulo} já existe.')
                input('Press any key to continue')
                titulo_existe = True
                break

        # Se não existir, adiciona
        if not titulo_existe:
            livros.append(dados)

            # Ordena os livros pelo título (sem acentos)
            livros.sort(key=lambda l: normalizar(l['titulo']))

            salvar_dados(livros)  # salva no JSON

            print(f'✅ {self.titulo} salvo com sucesso! 💾')
            input('\nPress any key to continue')

    # Marca livro como emprestado
    def levantar_livro(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"\n✅  {self.titulo} levantado com sucesso!")
        else:
            print(f"\n⚠️  {self.titulo} já está levantado")
        input('\nPress any key to continue...')

    # Marca livro como devolvido
    def devolver_livro(self):
        if self.disponivel:
            self.disponivel = False
            print(f"✅  {self.titulo} devolvido com sucesso.")
        else:
            print('O livro ja está emprestado.')
        input('\nPress any key to continue')


# Lista todos os livros
def listar_livros(livros):
    limpar_tela()

    if not livros:
        print('⚠️  Lista de livros vazia')
        input('\nPress any key to continue')
        return  # importante para não continuar

    print("=-=-="*11)
    print('\t\t📚LIVROS DISPONÍVEIS📚')

    # Percorre todos os livros
    for livro in livros:
        print("=-=-="*11)
        print(
            f"Titulo = {livro['titulo']}"
            f"\nAutor = {livro['autor']}"
            f"\nDisponibilidade = {livro['disponivel']}"
        )

    print("=-=-="*11)
    input('\nPress any key to continue...')


# 💻 MENU PRINCIPAL 💻
livros = carregar_dados()  # carrega dados ao iniciar

while True:
    limpar_tela()
    menu()

    try:
        opc = int(input('\nDigite sua opção: '))

        # Valida opção
        if opc < 1 or opc > 5:
            print('⚠️  Opção inválida!')
            input('Press any key to continue')
            continue

    except ValueError:
        print('⚠️  Opção inválida!')
        input('Press any key to continue')
        continue

    match opc:

        # ➕ Adicionar livro
        case 1:
            while True:
                titulo = input('Titulo do livro: ').lower()

                if not titulo.strip():
                    print('⚠️  Não pode ficar vazio.')
                else:
                    break

            while True:
                autor = input('Autor: ')

                # Valida se só tem letras e espaços
                if autor.replace(" ", "").isalpha():
                    break
                else:
                    print('⚠️  autor inválido')
                    input('\nPress any key to continue.')

            dados = sistema_biblioteca(titulo, autor)
            dados.adicionar_livro(livros)

        # 📋 Listar livros
        case 2:
            listar_livros(livros)

        # 📚 Levantar (emprestar)
        case 3:
            for i, livro in enumerate(livros, start=1):
                print(f"{i}. {livro['titulo']}")

            indice = int(input('Digite o índice do livro: '))
            livro_escolhido = livros[indice - 1]

            # Converte dict → objeto
            livro_obj = sistema_biblioteca(
                livro_escolhido['titulo'],
                livro_escolhido['autor'],
                livro_escolhido['disponivel']
            )

            # Empresta
            livro_obj.levantar_livro()

            # Atualiza lista
            livro_escolhido['disponivel'] = livro_obj.disponivel

            salvar_dados(livros)

        # 🔄 Devolver livro
        case 4:
            for i, livro in enumerate(livros, start=1):
                print(f"{i}. {livro['titulo']}")

            indice = int(input('Digite o índice do livro: '))
            livro_escolhido = livros[indice - 1]

            # Converte dict → objeto
            livro_obj = sistema_biblioteca(
                livro_escolhido['titulo'],
                livro_escolhido['autor'],
                livro_escolhido['disponivel']
            )

            # Devolve
            livro_obj.devolver_livro()

            # Atualiza lista
            livro_escolhido['disponivel'] = livro_obj.disponivel

            salvar_dados(livros)

        # ❌ Sair
        case 5:
            break