# Calculadora de Expressões

# Crie um programa que:

# Tenha uma função calcular(op, a, b) para realizar operações.

# Use um loop para permitir várias operações seguidas.

# Use condições para validar se a operação digitada é válida.

# Armazene o histórico de operações em um dicionário onde a chave é "operação 1", "operação 2", etc.

def calculadora(op, a, b):
    if op not in [0, 1, 2, 3]:
        return 'operação inválida! Tente novamente.'
    elif op == 1:
        return f'A soma de {a} + {b} = {a + b}'
    elif op == 2:
        if a > b:
            return f'A subtração de {a} - {b} = {a - b}'
        else:
            if b > a:
                return f'A subtração de {b} - {a} = {b - a}'
    elif op == 3:
        return f'A multiplicação de {a} x {b} = {a * b}'
    
    return None


historico = {}
contador = 1
while True:
    print("[1] para somar")
    print("[2] para subtrair")
    print("[3] para multiplicar")
    print("[0] para sair")
    operacao = int(input("Digite a operação que deseja: "))
    if operacao == 0:
        break
    
    n1 = int(input("digite um número:"))
    n2 = int(input("digite outro número:"))
    
    total = calculadora(operacao, n1, n2)

    #armazena o histórico

    historico[f'operacao {contador}'] = total
    contador += 1

#Mostra todo o histórico no final
for chave, valor in historico.items():
    print("=-" *30)
    print(f'{chave}: {valor}')

print("=-" *30)






    

    