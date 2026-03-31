# Classe que representa um carrinho de compras
class Carrinho:
    def __init__(self):
        # Lista privada para armazenar os produtos
        self._produtos = []

    # Método para inserir um ou vários produtos no carrinho
    def inserir_produto(self, *produtos):
        # Adiciona todos os produtos recebidos à lista
        self._produtos.extend(produtos)

        # Outra forma de fazer (comentada):
        # for produto in produtos:
        #     self._produtos.append(produto)

    # Método que calcula o total dos preços dos produtos
    def total(self):
        # Soma todos os preços dos produtos na lista
        return sum(produto.preco for produto in self._produtos)

    # Método para listar os produtos no carrinho
    def listar_produtos(self, *produtos):
        # Percorre todos os produtos e imprime nome e preço
        for produto in self._produtos:
            print(produto.nome, produto.preco)


# Classe que representa um produto
class Produto:
    def __init__(self, nome, preco):
        # Atributo para o nome do produto
        self.nome = nome
        # Atributo para o preço do produto
        self.preco = preco

    
# Criação de um objeto Carrinho
carrinho = Carrinho()

# Criação de três produtos
p1 = Produto('Computador', 1500)
p2 = Produto('Playstation', 450)
p3 = Produto('Monitor', 120)

# Inserção dos produtos no carrinho
carrinho.inserir_produto(p1, p2, p3)

# Espaçamento no terminal
print()

# Título da lista
print('LISTA DE PRODUTOS')
print()

# Listar todos os produtos do carrinho
carrinho.listar_produtos()

print()

# Mostrar o total formatado com 2 casas decimais
print('TOTAL:', end=' ')
print(f'{carrinho.total():.2f}€')