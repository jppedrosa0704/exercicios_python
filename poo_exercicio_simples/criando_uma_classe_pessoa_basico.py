# Atributos:
# nome
# idade
# 🔹 Métodos:
# apresentar() → deve imprimir algo como:
# "Olá, meu nome é João e tenho 25 anos."

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'olá, meu nome é {self.nome} e tenho {self.idade} anos.')

    def fazer_aniversario(self):
        self.idade += 1

p1 = pessoa('João', 25)
p1.apresentar()

p1.fazer_aniversario()
p1.apresentar()