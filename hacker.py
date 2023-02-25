"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    dicionario = {}
    res = []
    for (cc, mail) in log:
        if mail not in dicionario:
            dicionario[mail] = cc
        else:
            prev_cc = dicionario[mail]
            next_cc = ""
            for idx in range(len(prev_cc)):
                if cc[idx] != '*':
                    next_cc += cc[idx]
                else:
                    next_cc += prev_cc[idx]
                dicionario[mail] = next_cc
    for elem in dicionario:
        res.append(((dicionario.get(elem)), elem))
    res.sort(key=lambda x: (x[1], x[0]))
    res.sort(key=lambda y: y[0].count('*'))
    return res
    