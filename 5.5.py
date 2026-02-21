#TODO: segundo maior

def segundo_maior(l):
    if len(l) < 2:
        raise ValueError('A lista precisa ter pelo menos dois elementos')
    maior = max(l) #econtra o maior
    l_sem_maior = [x for x in l if x != maior]
    return max(l_sem_maior)

print(segundo_maior([1, 100]))
print(segundo_maior([-1, 20, 12, -10]))
