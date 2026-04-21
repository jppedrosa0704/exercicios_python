class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
            
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.professor_responsavel = None

    def __str__(self):
        prof = self.professor_responsavel.nome if self.professor_responsavel else "nenhum"
        return f"Nome: {self.nome} | idade: {self.idade} | Prof: {prof} "


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def __str__(self):
        return f"{self.nome} ({self.disciplina})"

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_alunos(self, lista_alunos):
        self.alunos.extend(lista_alunos)

    def listar_alunos(self):
        print("=-"*9)
        print(f"Lista da {self.nome} ")
        print("=-"*9)
        for aluno in self.alunos:
            print(f"Aluno: {aluno.nome}"
                f"\nIdade: {aluno.idade}"
                f"\nMatricula: {aluno.matricula}"
                f"\nprofessor: {aluno.professor_responsavel.nome}"
                f"\nDisciplina: {aluno.professor_responsavel.disciplina}"
            )
            print()

#Chamando instância
turma1 = Turma("Turma A")
turma2 = Turma("Turma B")

#chamando instância
a1 = Aluno('João', 40, 'A001')
a2 = Aluno('Ana', 33, 'A002')
a3 = Aluno('Priscila', 39, 'A003')
a4 = Aluno('jenyfer', 34, 'A004')
a5 = Aluno('Barbara', 25, 'A005')

#chamando instância professor
p1 = Professor('Rui', 58, 'Redes de computadores')
p2 = Professor('Fernando', 52, 'C++')
p3 = Professor('Guelhas', 65, 'Excel')
p4 = Professor('Frederico', 35, 'Java')


#Agregação
turma1.adicionar_alunos([a1, a2])
turma2.adicionar_alunos([a3, a4, a5])

#Associação aluno/professor
a1.professor_responsavel = p1
a2.professor_responsavel = p1
a3.professor_responsavel = p2
a4.professor_responsavel = p3
a5.professor_responsavel = p4

turma1.listar_alunos()
turma2.listar_alunos()


#lista de alunos cadastrados
# print("TURMA 1")
# for aluno in turma1.alunos:
#     print(f"Nome: {aluno.nome:<6} | idade: {aluno.idade} | matricula: {aluno.matricula} | professor: {aluno.professor_responsavel.nome}")
# print()
# print("TURMA 2")
# for aluno in turma2.alunos:
#     print(f"Nome: {aluno.nome:<6} | idade: {aluno.idade} | matricula: {aluno.matricula} | professor: {aluno.professor_responsavel.nome}")