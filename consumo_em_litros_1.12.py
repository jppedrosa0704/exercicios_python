#1.12 Escreva um programa que pergunte ao utilizador os quilómetros percor
# ridos e o número de litros de combustível que um automóvel gastou, e imprima
# o consumo em litros gastos aos 100 quilómetros.

km = int(input('Quantos km percorrido: '))
litros = int(input('Quantos litros consumidos: '))

media = (litros / km) * 100

print(f'consumo gasto em 100 km em litros foi {media:.2f} litros')