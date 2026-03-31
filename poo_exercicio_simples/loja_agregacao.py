# =========================================
# Projeto: Sistema de Loja em Python
# Descrição: Exemplo de POO com agregação.
# Autor: Seu Nome
# Requisitos:
# - Classe Produto com atributos nome e preco
# - Classe Loja que contém uma lista de produtos
# - Adicionar produtos à loja
# - Listar todos os produtos
# - Calcular o valor total dos produtos
# Conceito: Agregação (Loja agrega Produtos)
# =========================================

# Classe Loja representa o "carrinho/estoque" de produtos
class Loja:
    def __init__(self):
        # Lista interna de produtos da loja
        self._produtos = []
    
    # Método para adicionar um produto à loja
    def adicionar_produto(self, produto):
        self._produtos.append(produto)

    # Método para listar produtos com nome e preço
    def listar_produto(self):
        for produto in self._produtos:
            # Formata o preço com separador de milhares e duas casas decimais
            print(f"Produto: {produto.nome} Preço: {produto.preco:,.2f}")

    # Método para calcular o total de todos os produtos
    def total(self):
        valor = sum([produto.preco for produto in self._produtos])
        # Formata o valor no estilo europeu: separador de milhares ponto, decimal ponto
        valor_formatado = f"{valor:,.2f}".replace(',', '.')
        return f"Total: {valor_formatado}€"


# Classe Produto representa um item que pode ser adicionado à loja
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Menu inicial
print('[1] Adicionar produto')
print('[2] Listar produtos')
print('[3] Total dos produtos')
print('[4] Sair')

# Criando a instância da loja uma vez (agregação)
loja = Loja()

# Loop principal do menu
while True:
    try:
        opc = int(input('Digite a opção desejada: '))
        if opc < 1 or opc > 4:
            print("Opção inválida")
            continue
    except ValueError:
        print("Opção inválida")
        continue

    match opc:
        case 1:
            # Adicionar produtos à loja
            qtd = int(input('Quantidade de produtos? '))
            for p in range(qtd):
                nome = str(input('Nome: '))
                preco = float(input('Preço: '))
                # Cria o produto (independente da loja)
                produto = Produto(nome, preco)
                # Adiciona o produto à loja (agregação)
                loja.adicionar_produto(produto)
        case 2:
            # Lista todos os produtos da loja
            loja.listar_produto()
        case 3:
            # Mostra o valor total dos produtos
            print(loja.total())
        case 4:
            # Sai do programa
            break