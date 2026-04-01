# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


# Definição da classe Carro
class Carro:
    # Método construtor (executado quando um objeto é criado)
    def __init__(self, nome):
        self.nome = nome              # Nome do carro
        self._motor = None            # Motor começa como None (privado por convenção)
        self._fabricante = None       # Fabricante começa como None (privado por convenção)

    # Getter para fabricante (permite acessar como atributo)
    @property
    def fabricante(self):
        return self._fabricante       # Retorna o fabricante

    # Setter para fabricante (permite definir valor com validação futura, se quiser)
    @fabricante.setter
    def fabricante(self, valor):
        # Validação: só aceita objetos do tipo Fabricante
        if not isinstance(valor, Fabricante):
            raise TypeError('fabricante precisa ser do tipo Fabricante')
        self._fabricante = valor      # Define o fabricante

    # Getter para motor
    @property
    def motor(self):
        return self._motor            # Retorna o motor

    # Setter para motor
    @motor.setter
    def motor(self, valor):
        # Validação: só aceita objetos do tipo Motor
        if not isinstance(valor, Motor ):
            raise TypeError('motor precisa ser do tipo Motor.')
        self._motor = valor           # Define o motor


# Classe Motor
class Motor:
    def __init__(self, nome):
        self.nome = nome              # Nome do motor (ex: 1.0, 2.0, etc)


# Classe Fabricante
class Fabricante:
    def __init__(self, nome):
        self.nome = nome              # Nome da fabricante (ex: Volkswagen)


# Criando um objeto Carro chamado 'fusca'
fusca = Carro('Fusca')

# Criando um objeto Fabricante
volkswagen = Fabricante('Volkswagen')

# Criando um objeto Motor
motor_1_0 = Motor('1.0')


# Atribuindo diretamente (não recomendado, pois ignora os setters)
fusca.fabricante = volkswagen
fusca.motor = motor_1_0


# Exibindo os dados
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)