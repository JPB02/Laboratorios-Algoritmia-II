'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    res = {}
    for rua in ruas:
        if rua[0] not in res:
            res[rua[0]] = 0
        if rua[-1] not in res:
            res[rua[-1]] = 0
        if rua[0] in res:
            if rua[0] == rua[-1]:
                res[rua[0]] += 1
            else:
                res[rua[0]] += 1
                res[rua[-1]] += 1
    x = sorted(res.items(), key=lambda x:(x[1],x[0]))
    return x

