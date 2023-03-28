'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

def chunks(rotas):
    rotas_chunk = []
    for element in rotas:
        idx = 0
        if len(element) == 3:
            rotas_chunk.append(element)
        else:
            while idx <= len(element)-3:
                rotas_chunk.append(list((element[idx],element[idx+1],element[idx+2])))
                idx +=2
    return rotas_chunk

def build(arestas):
    adj = {}
    for o,p,d in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj

def viagem(rotas,o,d):
    adj = build(chunks(rotas))
    dist = {}
    for x in adj:
        dist[x] = {}
        for y in adj:
            if x == y:
                dist[x][y] = 0
            elif y in adj[x]:
                dist[x][y] = adj[x][y]
            else:
                dist[x][y] = float("inf")
    for k in adj:
        for x in adj:
            for y in adj:
                if dist[x][k] + dist[k][y] < dist[x][y]:
                    dist[x][y] = dist[x][k] + dist[k][y]
    return dist[d][o]


rotas = [
         ["Porto",20,"Lisboa"],
         ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
         ["Braga",3,"Famalicao",3,"Porto"],
         ["Viana",4,"Povoa",3,"Porto"],
         ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
        ]

print("Output: ", viagem(rotas,"Caminha","Lisboa"))
print("Solução: " + "30")