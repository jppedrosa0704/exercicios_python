num_pares = []
while True:
    try:
        numero = int(input('Digite um número: '))
        break
    except ValueError:
        print('Digite apenas números.')
        
for i in range(numero + 1):
    if i % 2 == 0:
        if i > 0:
            num_pares.append(i)


print(num_pares)



