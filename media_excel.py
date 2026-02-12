import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

data = {
    'students': [
        
        {'nome': 'Ana', 'notas': [8, 10, 11, 10, 12]},
        {'nome': 'João', 'notas': [10, 12, 12, 9, 10]},
        {'nome': 'Luiza', 'notas': [14, 13, 14, 14, 13]},
        {'nome': 'Paulo', 'notas': [18, 17, 17, 19, 18]},
        {'nome': 'Pedro', 'notas': [9, 8, 9, 9, 10]},
        {'nome': 'Tereza', 'notas': [14, 15, 16, 15, 16]}
        
    ]
}

limpar_tela()
lista_media = []
for i, a in enumerate(data['students'], start=1):
    print("====="*10)
    media = (sum(a['notas']) / len(a['notas']))
        
    if media < 10:
        status = 'Failed'
        print(f"{i}. Nome: {a['nome']:<8} Média: {media:<5.2f}  status: {status}")
    else:
        status = 'Approved'
        print(f"{i}. Nome: {a['nome']:<8} Média: {media:<5.2f}  status: {status}")

    lista_media.append(media)
print("====="*10)

print(f"Highest average was: {max(lista_media):.2f}")
print(f"Lowest average was: {min(lista_media):.2f}")
