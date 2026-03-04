'''3.2 Utilizando a função range, escreva um programa que imprime os valores
10, 13, 16,..., 55.
(a) Usando a instrução break, modifique-o para terminar o ciclo quando en
contrar um múltiplo de 7.
(b) Usando a instrução continue, modifique-o para não imprimir valores múl
tiplos de 7.'''

# for i in range(10, 56, 3):
#     print(i)

#A

for i in range(10, 56, 3):
    if i % 7 == 0:
        print(f'{i} é multiplo de 7. \nFIM!')
        break
    print(i)


#B
for i in range(10, 56, 3):
    if i % 7 != 0:
        print(f'{i}')
        continue
    
    
