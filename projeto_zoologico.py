# PROJETO -- ZOOLÓGICO.

# Objetivo: Gerenciamento de um Zoológico.

# -----------------------------------------------

# Interface com Menu contendo 5 opções.

#  -- Adicionar Animal
#  -- Remover Animal
#  -- Mudar Animal
#  -- Listar Animais
#  -- Sair do Programa

# -----------------------------------------------

# 1. Adicionar Animal -> Adicionar um animal ao final do Array (Animal não pode já existir no array)

# 2. Remover Animal -> User escolhe o animal que quer ser removido. (O animal tem de existir no array)

# 3. Mudar Animal -> User escolhe um animal no array e o substitui por outro.

# 4. Listar Animais -> Imprime todos os animais do array.
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar_animal(animal, animais):
    if animal in animais:
        limpar_tela()
        print( f"⚠️  '{animal} já consta na lista.'")
        return
    
    if animal == "":
        limpar_tela()
        print("⚠️  Não pode conter espaços.")
        return
    
    if not animal.isalpha():
        limpar_tela()
        print("⚠️  O nome do animal não pode conter números ou símbolos.")
        return
    
    limpar_tela()
    animais.append(animal)
    print("=-" *30)
    print(f"'{animal}' adicionado com sucesso.")

def remover_animal(animal, animais):
    if animal == "":
        print("Não pode conter espaços.")
        return
    if animal < 1 or animal > len(animais):
        print("⚠️  Não consta na lista")
        return
    
    limpar_tela()
    animal_removido = animais[animal -1]
    del animais[animal -1]
    print("=-" *30)
    print(f"{animal_removido} removido com sucesso.")

def substituir_animal(animal, animais):
    if animal == "":
        print("Não pode conter espaços.")
    if animal < 1 or animal > len(animais):
        print("⚠️  Não consta na lista")
    else:
        animais[animal-1] in animais
        novo_animal = input("Digite o animal que deseja adicionar: ").title()
        animais[animal-1] = novo_animal
        limpar_tela()
        print(f"'{novo_animal}' adicionado com sucesso.")

def listar_animais():
    limpar_tela()
    print("=-" *30)
    print('LISTA DE ANIMAIS DISPONÍVEIS')
    print("=-" *30)
    print(", ".join(animais) + ".")
    print("=-" *30)

def codigo_animais():
    print("=-" *30)
    print("COD | ANIMAIS")
    for indice, animal in enumerate(animais):
        print(f" {indice+1}  | {animal}")
    print("=-" *30)


limpar_tela()

#Lista de animais do zoologico.
animais = ['Leão', 'Girafa', 'Macacopes']

while True:
    print("=-" *30)
    print(f"{'PROJETO ZOOLÓGICO':^60}")
    print("=-" *30)
    print(f"{"[1] Adicionar animal":>40}")
    print(f"{'[2] Remover Animal':>38}")
    print(f"{'[3] Mudar Animal':>36}")
    print(f"{'[4] Listar Animais':>38}")
    print(f"{'[5] Sair do Programa':>40}")
    print("=-" *30)
    try:
        opção = int(input('Digite sua opção: '))
    except ValueError:
        limpar_tela()
        print('⚠️  Digite uma opção válida.')
        continue

    if opção < 1 or opção > 5:
        print('⚠️  Digite uma opção válida.')
    if opção == 1:
        animal = input("Digite o animal que deseja adicionar: ").title()
        adicionar_animal(animal, animais)

    elif opção == 2:
        limpar_tela()
        codigo_animais()
        
        while True:
            try:
                animal = int(input("Digite o código do animal que deseja remover: "))
                break
            except ValueError:
                print("Digite um código válido")
                continue
        
        remover_animal(animal, animais)

    elif opção == 3:
        limpar_tela()
        codigo_animais()
        while True:
            try:
                animal = int(input("Digite o código do animal para substituir: "))
                
                break
            except ValueError:
                print("Digite um código válido.")
                continue
        
        substituir_animal(animal, animais)

    elif opção == 4:
        listar_animais()

        while True:
            resp = input("quer continuar? [S/N] ").upper()
            if resp not in ("S", "N"):
                print("⚠️  Digite 'S' para sim e 'N' para não.")
                continue
            else:
                break
        if resp == 'N':
            break


    elif opção == 5:
        print('✋ Programa encerrado.')
        break

print("=-" *30)
print(F"{'RESUMO DO PROGRAMA':^60}")
print("=-" *30)
print(f"Lista de animais: {animais}")
print(f"Quantidade de animais: {len(animais)} ")
print("=-" *30)