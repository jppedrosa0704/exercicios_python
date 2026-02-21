# TODO: (b) Um número inteiro é perfeito se for igual à soma dos seus divisores
#  próprios. Exemplo: 6 é perfeito porque 6 = 1 + 2 + 3 mas 10 não é porque
# 10= 1+2+5. Escreva uma função perfeito(n) que testa se n é perfeito
# ou não; o resultado deve ser um valor lógico.

def divisor(n):
    num = [k for k in range(1, n + 1) if n % k == 0]
    num.remove(max(num))
    return num

def divisor_perfeito(n):
    perfeito = sum(divisor(n))
    if perfeito == n:
        return True
    return False

n = 6

print(f'Dividores de {n}:', divisor(n))
print(f'{n} é: {divisor_perfeito(n)}')
