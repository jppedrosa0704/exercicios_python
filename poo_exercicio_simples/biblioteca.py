class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade inválida.")

    def mostrar_dados(self):
        print(f"Nome: {self.__nome} | Idade: {self.__idade}")


class Usuario(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.append(livro)
            print(f"{livro.titulo} emprestado com sucesso!")
        else:
            print(f"{livro.titulo} não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.disponivel = True
            self.livros_emprestados.remove(livro)
            print(f"{livro.titulo} devolvido com sucesso.")
        else:
            print("Você não possui esse livro.")

    def mostrar_dados(self):
        super().mostrar_dados()

        if self.livros_emprestados:
            print("Livros emprestados:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")
        else:
            print("Nenhum livro emprestado.")


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def mostrar_info(self):
        status = 'Disponível' if self.disponivel else 'Indisponível'
        print(f"{self.titulo} | {self.autor} | {status}")


# TESTE
livro1 = Livro('Python', 'João')
livro2 = Livro('POO', 'Pythonildo')

user = Usuario('Fatima', 25)

user.emprestar_livro(livro1)
user.emprestar_livro(livro2)

user.mostrar_dados()

user.devolver_livro(livro1)
user.mostrar_dados()