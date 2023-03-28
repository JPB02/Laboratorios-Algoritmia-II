from itertools import combinations

artigos = {
    "Adaptive register allocation with a linear number of registers": {
        "Carole Delporte-Gallet",
        "Hugues Fauconnier",
        "Eli Gafni",
        "Leslie Lamport"
    },
    "Oblivious collaboration": {
        "Yehuda Afek",
        "Yakov Babichenko",
        "Uriel Feige",
        "Eli Gafni",
        "Nati Linial",
        "Benny Sudakov"
    },
    "Optima of dual integer linear programs": {
        "Ron Aharoni",
        "Paul Erdos",
        "Nati Linial"
    }
}

def create_partnerships (artigos):
    partnerships = []
    for title in artigos:
        authors = artigos[title]
        p_combs = list(combinations(authors, 2))
        f_combs = [ (y, x) for (x, y) in p_combs ]
        for combination in p_combs:
            f_combs.append(combination)
        for combination in f_combs:
            if combination not in partnerships:
                partnerships.append(combination)
    return partnerships

def build(arestas):
    adj = {}
    for o,d in arestas:
        if o not in adj:
            adj[o] = set()
        if d not in adj:
            adj[d] = set()
        adj[o].add(d)
        adj[d].add(o)
    return adj

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai

def caminho(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho

def create_erdos_list (artigos, n):
    partnerships = create_partnerships(artigos)
    graph = build(partnerships)
    authors = list(graph.keys())
    erdos_colab = []
    for author in authors:
        n_erdos = len(caminho(graph, author, "Paul Erdos")) - 1
        if n_erdos <= n:
            erdos_colab.append((author, n_erdos))
    return erdos_colab

def erdos (artigos, n):
    erdos_colab = create_erdos_list(artigos, n)
    erdos_sorted = sorted(erdos_colab, key = lambda e : (e[1], e[0]))
    return [ x for (x, y) in erdos_sorted]

print(erdos(artigos, 2))
print("['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek'])")