num_pares = []
while True:
    '''
    Peça ao usuário um número inteiro positivo.
    Use while para mostrar todos os números pares de 0 até esse número.
    '''
    try:
        numero = int(input('Digite um número: '))
        break
    except ValueError:
        print('Digite apenas números.')

i = 0
while i < numero + 1:
    if i % 2 == 0:
        if i > 0:
            num_pares.append(i)
    i += 1
        
#for i in range(numero + 1):
#    if i % 2 == 0:
#       if i > 0:
#            num_pares.append(i)

print(num_pares)






