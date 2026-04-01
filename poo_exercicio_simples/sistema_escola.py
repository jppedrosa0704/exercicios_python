'''Crie as classes:
- Aluno (nome)
- Professor (nome)
- Turma (nome)

Regras:
- Uma turma tem um professor
- Uma turma tem vários alunos
- Um aluno pode estar em uma turma'''

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self._professor = None
        self._alunos = []

    def cadastrar_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError('deve ser um objeto Aluno')
        self._alunos.append(aluno)

    def listar_alunos(self):
        limpar_tela()
        if not self._alunos:
            print('Não tem alunos cadastrados')
            # input('pres any key to continue...')
        else:
            for aluno in self._alunos:
                print('============='*3)
                print(f"Turma: {self.nome}")
                print(f"Aluno: {aluno.nome}")
                print(f"Professor: {self.professor.nome if self.professor else 'Não definido'}")
            print('============='*3)
        input('\npress any key to continue')

    
    @property
    def professor(self):
        return self._professor
    @professor.setter
    def professor(self, valor):
        if not isinstance:
            raise TypeError('professor deve ser do tipo Professor')
        self._professor = valor

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Professor:
    def __init__(self, nome):
        self.nome = nome

turma = Turma('Programação em Python') #criando objeto turma
# aluno1 = Aluno('João Paulo Pedrosa Soares') #Criando objeto aluno
professor = Professor('Pythonildo da silva') #Criando objeto professor
turma.professor = professor #Ligação entre a turma e o professor

while True:
    limpar_tela()
    print(f'Cadastrar aluno no curso: {turma.nome}')
    print('[1] cadastrar aluno')
    print('[2] listar alunos')
    print('[3] Sair')
    opc = int(input('Escolha a opção desejada: '))
    match opc:
        case 1:
            nome_do_aluno = input('Nome do aluno: ')
            aluno = Aluno(nome_do_aluno)
            turma.cadastrar_aluno(aluno)
        case 2:
            turma.listar_alunos()
        case 3:
            break

# turma.aluno = aluno1

