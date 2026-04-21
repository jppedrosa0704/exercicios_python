import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Dono(Pessoa):
    def __init__(self, nome, idade, telefone):
        super().__init__(nome, idade)
        self.telefone = telefone
        self.lista_animais = []

    def adicionar_animal(self, animal):
        self.lista_animais.append(animal)
    #dono (associação com Dono)
    #veterinário responsável (associação com Veterinário)

class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.veterinario_responsavel = None
        self.dono = None

    def __str__(self):
        return f"{self.nome} ({self.especie}, {self.idade} anos)"

class Veterinario(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self.especialidade = especialidade

class Clinica:
    def __init__(self, nome):
        self.nome = nome
        self.veterinarios = []
        self.animais = []
    
    def adicionar_veterinario(self, veterinario):
        self.veterinarios.append(veterinario)

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        print(f"===Animais da clínica {self.nome}===")
        for animal in self.animais:
            print(f"\nNome: {animal.nome}"
                f"\nEspécie: {animal.especie}"
                f"\nDono(a): {animal.dono.nome}"
                f"\nVeterinário: {animal.veterinario_responsavel.nome}"
                f"\nEspecialidade: {animal.veterinario_responsavel.especialidade}"
        )


    #métodos: adicionar_veterinario(vet)
    #adicionar_animal(animal)
    #listar_animais()

#Chamando instâncias da Classe Dono
d1 = Dono('João Paulo', 40, '913902521')
d2 = Dono('Felipe Herique', 40, '925412548')
d3 = Dono('Ana Medeiros', 33, '987456321')
d4 = Dono('Jenyfer Muller', 34, '913458721')
d5 = Dono('Libia Danielle', 47, '916587521')
d6 = Dono('Natalia Muller', 42, '985742521')

#Chamando instâncias da classe Animal
a1 = Animal('Ruckinho', 12, 'Cachorro')
a2 = Animal('Mimi', 5, 'Gato')
a3 = Animal('Oliver', 4, 'Gato')
a4 = Animal('Bunny', 12, 'Gato')
a5 = Animal('Seraphine Bolseira', 13, 'gato')
a6 = Animal('Louro José', 12, 'Papagaio')
a7 = Animal('Donald', 12, 'Pato')

#Associação animal / Dono
a1.dono = d1
d1.adicionar_animal(a1) #Agregação
a2.dono = d2
d2.adicionar_animal(a2) #Agregação
a3.dono = d3
d3.adicionar_animal(a3) #Agregação
a4.dono = d3
d3.adicionar_animal(a4) #Agregação
a5.dono = d4
d4.adicionar_animal(a5) #Agregação
a6.dono = d5
d5.adicionar_animal(a6) #Agregação
a7.dono = d6
d6.adicionar_animal(a7) #Agregação


#chamando instância Veterinario
petcare = Clinica('Pet Care')
v1 = Veterinario('Franciso Silva', 47, 'Animais exóticos')
v2 = Veterinario('Juberaldo da Jujubanes', 33, 'Felinos')
v3 = Veterinario('Astrogildo Astral', 33, 'Cirurgia')
v4 = Veterinario('Astrogildo Astral', 33, 'Aves')

#Associar Animal ao veterinario responsavel
a1.veterinario_responsavel = v1
a2.veterinario_responsavel = v3
a3.veterinario_responsavel = v2
a4.veterinario_responsavel = v2
a5.veterinario_responsavel = v2
a6.veterinario_responsavel = v4
a7.veterinario_responsavel = v4


#Agregando veterinários a lista de veterinários na classe Clinica
petcare.adicionar_veterinario(v1)
petcare.adicionar_veterinario(v2)
petcare.adicionar_veterinario(v3)
petcare.adicionar_veterinario(v4)

#Agregando animais a lista de animais na classe Clinica
petcare.adicionar_animal(a1)
petcare.adicionar_animal(a2)
petcare.adicionar_animal(a3)
petcare.adicionar_animal(a4)
petcare.adicionar_animal(a5)
petcare.adicionar_animal(a6)
petcare.adicionar_animal(a7)

#chamando metodos listar animais
petcare.listar_animais()
