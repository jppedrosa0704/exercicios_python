# Exercício: Animais
# 1 -Crie uma classe base chamada Animal que tenha:
# > Um atributo nome
# > Um método falar() que imprime "Este animal faz um som"
# 2 - Crie duas classes filhas que herdam de Animal:
# > Cachorro – o método falar() deve imprimir "Au Au!"
# > Gato – o método falar() deve imprimir "Miau!"
# Crie instâncias de Cachorro e Gato e chame o método falar() de cada uma.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def metodo_falar(self):
        print('Este animal faz um som')

# Classe filha Cachorro
class Cachorro(Animal):
    def metodo_falar(self):
        print('Au Au!')

# Classe filha Gato
class Gato(Animal):
    def metodo_falar(self):
        print('Miauuu.')

# Classe filha Vaca
class Vaca(Animal):
    def metodo_falar(self):
        super().metodo_falar() # Chama o método da classe base

#criando instâncias
meu_cachorro = Cachorro('Rex')
meu_gato = Gato('Mimi')
minha_vaca = Vaca('Vaca leitera')

# Chamando métodos
meu_cachorro.metodo_falar()  # Au Au!
meu_gato.metodo_falar()       # Miauuu.
minha_vaca.metodo_falar()     # Este animal faz um som

