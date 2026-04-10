#classe base
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

#Classe Filha
class Leao(Animal):
    def __init__(self, nome, idade, forca):
        super().__init__(nome, idade)
        self.forca = forca

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Força: {self.forca}")

#Classe Filha
class Elefante(Animal):
    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade)
        self.peso = peso

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Peso: {self.peso}Kg")

#Crirando instâncias
leao = Leao('Leão', 12, 'Feroz')
#Chamando métodos
leao.mostrar_info()
print() #quebra de linha
#Crirando instâncias
elefante = Elefante('Elefante', 22, 278)
#Chamando métodos
elefante.mostrar_info()