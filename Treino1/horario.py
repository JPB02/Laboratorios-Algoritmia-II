"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def overlap(horario):
    aux = []
    for (dia,hora,duracao) in horario:
        for i in range(0,duracao+1):
            aux.append((dia,hora+i))
    for tpl in aux:
        if aux.count(tpl) > 1:
            return True
    return False

def horario (ucs, alunos):
    res = []
    for aluno in alunos:
        hsemanal = []
        sum_ = 0
        invalido = False 
        cadeiras = alunos[aluno]
        for cadeira in cadeiras:
            if cadeira in ucs.keys():
                hsemanal.append(ucs[cadeira])
                sum_ += ucs[cadeira][2]
            else:
                invalido = True
        if (not invalido) and (not overlap(hsemanal)):
            res.append((aluno, sum_))
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1],reverse=True)
    return res