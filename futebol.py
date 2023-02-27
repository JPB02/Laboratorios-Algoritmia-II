 def tabela (jogos):
    res = {}
    sof = {}

    for (e1, a, e2, b) in jogos:
        if e1 not in sof:
            sof[e1] = 0
        if e2 not in sof:
            sof[e2] = 0
        
        sof[e1] += a-b
        sof[e2] += b-a

    for (e1, a, e2, b) in jogos:
        if e1 not in res:
            res[e1] = 0
        if e2 not in res:
            res[e2] = 0
        if a > b:
            res[e1] += 3
        elif a == b:
            res[e1] += 1
            res[e2] += 1
        else:
            res[e2] += 3

    final = list(res.items())

    final.sort(key=lambda x: x[0]) 
    final.sort(key=lambda x: sof[x[0]],reverse=True)
    final.sort(key=lambda x: res[x[0]],reverse=True)

    return final
        
