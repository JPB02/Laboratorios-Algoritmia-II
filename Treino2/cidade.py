'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
 
#Grafo Pesado

def make_l(lst):
    l = []
    for elem in lst:
        c1 = elem[0]
        c2 = elem[-1]
        l.append((c1,c2,len(elem)))
    return l

def build(arestas):
    adj = {}
    for o,d,p in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj


def tamanho(ruas):
    adj = build(make_l(ruas))
    o = ruas[0][0]
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
    return max(dist.values())

ruas1 = [
         "raio",
         "central",
         "liberdade",
         "chaos",
         "saovictor",
         "saovicente",
         "saodomingos",
         "souto",
         "capelistas",
         "anjo",
         "taxa"
        ]

ruas = [
        "ab",
        "bc",
        "bd",
        "cd"
       ]

print("Output: ", tamanho(ruas1))
print("Solução: " + "25")

print("Output: ", tamanho(ruas))
print("Solução: " + "4")