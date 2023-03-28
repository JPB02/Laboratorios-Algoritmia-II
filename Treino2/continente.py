'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def continentes(vizinhos,pais):
    lst_viz = [pais]
    for elem in vizinhos:
        if elem[0] in lst_viz:
            for pais in elem[1:]:
                lst_viz.append(pais)
    return lst_viz

def todos(vizinhos):
    t_paises = []
    for elem in vizinhos:
        for pais in elem:
            if pais not in t_paises:
                t_paises.append(pais)
    return t_paises

def maior(vizinhos):
    sol = 0
    res = [continentes(vizinhos,todos(vizinhos)[0])]
    for pais in todos(vizinhos)[1:]:
        for elem in res:
            if pais not in elem:
                res.append(continentes(vizinhos,pais))
    for cont in res:
        if len(cont) > sol:
            sol = len(cont)
    return sol

vizinhos = [
            ["Portugal","Espanha"],
            ["Espanha","França"],
            ["França","Bélgica","Alemanha","Luxemburgo"],
            ["Canada","Estados Unidos"]
            ]


print("Output: ", maior(vizinhos))
print("Solução: " + "6")