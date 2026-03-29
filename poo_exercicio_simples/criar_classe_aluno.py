import json

class Aluno:
    lista_alunos = []
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    @classmethod
    def salvar_dados(cls, caminho='CriandoClasseAlunos.json'):
        try:
            with open(caminho, 'w', encoding='utf-8') as arquivo:
                # 🔥 Você precisa salvar a lista de alunos convertida para dicionários:
                return json.dump(
                    [a.__dict__ for a in cls.lista_alunos],
                    arquivo,
                    ensure_ascii=False,
                    indent=2
                    )
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    @classmethod
    def carregar_dados(cls, caminho='CriandoClasseAlunos.json'):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                cls.lista_alunos = [Aluno(**d) for d in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    @classmethod
    def listar_alunos(cls):
        if not cls.lista_alunos:
            print('⚠️  Nenhum aluno cadastrado.')
            return
        
        for aluno in cls.lista_alunos:
            # status = "Aprovado" if aluno.aprovado() else "Reprovado"
            if aluno.aprovado():
                status = 'Aprovado'
            else:
                status = 'Reprovado'

            print(
                f'Nome: {aluno.nome}\n'
                f'Idade: {aluno.idade}\n'
                f'Nota: {aluno.notas}\n'
                f'status: {status}\n'
                )
            
    
    def aprovado(self):
        return self.notas >= 10
            
        

Aluno.carregar_dados()

while True:
    print('[1] Adicionar Aluno')
    print('[2] Listar Aluno')
    print('[3] Sair')
    try:
        opc = int(input('\nescolha uma das opções: '))
        if opc <1 or opc > 3:
            print('⚠️ Opção inválida.')
            input('\nPress any key to continue...')
            continue
    except ValueError():
        print('⚠️ Opção inválida.')
        input('\nPress any key to continue...')
        continue
    match opc:
        case 1:
            nome = input('Nome: ').strip()
            idade = int(input('idade: '))
            notas = float(input('notas: '))

            aluno = Aluno(nome, idade, notas)
            Aluno.lista_alunos.append(aluno)
            Aluno.salvar_dados()
        case 2:
            Aluno.listar_alunos()
        case 3:
            break
    continuar = input('Quer continuar? [S/N]').lower()
    if continuar in ('s', 'n'):
        if continuar == 's':
            continue
    if continuar == 'n':
        break
        




