#classe base
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        print(f"nome: {self.nome}, Salário: {self.salario:.2f}€")

#classe filha gerente
class Gerente(Funcionario):
    #reaproveita o construtor da classe base
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def mostrar_dados(self):
        salario_total = self.salario + self.bonus
        valor_formatado = f"{salario_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Nome: {self.nome} | Salário com bônus: {valor_formatado}€")

#classe filha Estagiario
class Estagiario(Funcionario):
    def __init__(self, nome, salario, horas_trabalhadas):
        super().__init__(nome, salario)
        self.horas_trabalhadas = horas_trabalhadas

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | horas trabalhadas: {self.horas_trabalhadas}")

#Criando instâncias:
gerente = Gerente('João', 3000, 850)
estagiario = Estagiario('Ana', 1500, 30)

#Chamando métodos

gerente.mostrar_dados()
estagiario.mostrar_dados()