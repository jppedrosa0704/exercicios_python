#Exercício 5 – Ciclo com condição ternária

#Imprimir números de 1 a 10 indicando se são pares ou ímpares

def par_ou_impar(num):
    for n in range(num):
        print(n, 'é', 'par' if n % 2 == 0  else 'impar')

par_ou_impar(11)