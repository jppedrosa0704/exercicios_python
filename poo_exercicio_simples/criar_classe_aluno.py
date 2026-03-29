import json  # importa módulo para trabalhar com JSON (salvar e carregar dados)

class Aluno:
    lista_alunos = []  # lista da classe que guarda todos os alunos (compartilhada)

    def __init__(self, nome, idade, notas):
        # construtor → cria um novo objeto aluno
        self.nome = nome
        self.idade = idade
        self.notas = notas

    @classmethod
    def salvar_dados(cls, caminho='CriandoClasseAlunos.json'):
        # método da classe → salva todos os alunos no arquivo JSON
        try:
            with open(caminho, 'w', encoding='utf-8') as arquivo:
                # converte cada objeto aluno para dicionário usando __dict__
                # e salva no JSON formatado (indent=2 deixa legível)
                return json.dump(
                    [a.__dict__ for a in cls.lista_alunos],
                    arquivo,
                    ensure_ascii=False,  # permite acentos
                    indent=2  # formata o JSON bonitinho
                )
        except FileNotFoundError:
            # erro caso o arquivo não exista (pouco provável aqui)
            return []
        except json.JSONDecodeError:
            # erro de leitura de JSON (mais comum no load, não no dump)
            return []
    
    @classmethod
    def carregar_dados(cls, caminho='CriandoClasseAlunos.json'):
        # método da classe → carrega os dados do JSON
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)  # lê JSON → vira lista de dicionários
                
                # reconstrói os objetos Aluno a partir dos dicionários
                cls.lista_alunos = [Aluno(**d) for d in dados]
        except FileNotFoundError:
            # se o arquivo não existir, começa com lista vazia
            return []
        except json.JSONDecodeError:
            # se o JSON estiver corrompido
            return []
    
    @classmethod
    def listar_alunos(cls):
        # método da classe → lista todos os alunos
        
        if not cls.lista_alunos:
            print('⚠️  Nenhum aluno cadastrado.')
            return
        
        for aluno in cls.lista_alunos:
            # verifica se o aluno está aprovado ou reprovado
            if aluno.aprovado():
                status = 'Aprovado'
            else:
                status = 'Reprovado'

            # imprime os dados formatados
            print(
                f'Nome: {aluno.nome}\n'
                f'Idade: {aluno.idade}\n'
                f'Nota: {aluno.notas}\n'
                f'Status: {status}\n'
            )
    
    def aprovado(self):
        # método do objeto → verifica se o aluno passou
        return self.notas >= 10


# 🔹 carrega os dados do arquivo ao iniciar o programa
Aluno.carregar_dados()

# 🔹 loop principal (menu)
while True:
    print('[1] Adicionar Aluno')
    print('[2] Listar Aluno')
    print('[3] Sair')

    try:
        # tenta ler a opção do usuário
        opc = int(input('\nescolha uma das opções: '))
        
        # valida se está dentro das opções válidas
        if opc < 1 or opc > 3:
            print('⚠️ Opção inválida.')
            input('\nPress any key to continue...')
            continue

    except ValueError():
        # erro caso o usuário digite algo que não é número
        print('⚠️ Opção inválida.')
        input('\nPress any key to continue...')
        continue

    match opc:
        case 1:
            # adiciona um novo aluno
            nome = input('Nome: ').strip()
            idade = int(input('idade: '))
            notas = float(input('notas: '))

            aluno = Aluno(nome, idade, notas)  # cria objeto
            Aluno.lista_alunos.append(aluno)  # adiciona na lista
            Aluno.salvar_dados()  # salva no JSON

        case 2:
            # lista todos os alunos
            Aluno.listar_alunos()

        case 3:
            # sai do programa
            break

    # pergunta se quer continuar
    continuar = input('Quer continuar? [S/N]').lower()

    if continuar in ('s', 'n'):
        if continuar == 's':
            continue

    if continuar == 'n':
        break
