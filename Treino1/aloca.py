"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def f(l1,l2):
    for x in l1:
        if x not in l2:
            return x

def aloca(prefs):
    res = []
    aux = []
    sorted_keys = sorted(prefs.keys())
    
    for key in sorted_keys:
        prefs.update({key:f(prefs.get(key), aux)})
        aux.append(prefs.get(key))
        
    for i in prefs:
        if prefs[i] == None:
            res.append(i)
    
    return sorted(res)