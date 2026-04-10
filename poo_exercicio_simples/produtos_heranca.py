class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        preco = (f"{self.preco:,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Produto: {self.nome} | Preço: {preco}€")

class Produto_Com_Desconto(Produto):
    def __init__(self, nome, preco, desconto):
        super().__init__(nome, preco)
        self.desconto = desconto

    def mostrar_preco(self):
        super().mostrar_preco()
        desconto_total = (f"{self.preco - (self.preco * self.desconto / 100):,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Valor do produto com desconto: {desconto_total}€")

class ProdutoComFrete(Produto):
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def mostrar_preco(self):
        super().mostrar_preco()
        valor_total = (f"{self.preco + self.frete:,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"valor do produto com frete: {valor_total}€")

#Criando instâncias
produto_com_desconto = Produto_Com_Desconto('Super Bock', 1000, 5)
produto_com_desconto.mostrar_preco()
print()
#Chamando métodos
produto_com_frete = ProdutoComFrete('Laptop', 1500, 60)
produto_com_frete.mostrar_preco()

