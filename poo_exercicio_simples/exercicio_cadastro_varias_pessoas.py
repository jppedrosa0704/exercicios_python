class Pessoa:
    def __init__(self, idde, pessoa):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome}, {self.idade} anos'
        
pessoas = []

while True:
    nome = input('nome: ')
    try:
        idade = int(input('idade: '))
    except ValueError:
        print('opção inválida.')

    pessoa = {'nome': nome, 'idade': idade}
    pessoas.append(pessoa)

    continuar = input('Quer continuar? [s/n]').lower()
    if continuar != 's':
        break

for p in pessoas:
    print(f'{p['nome']}, {p['idade']}')