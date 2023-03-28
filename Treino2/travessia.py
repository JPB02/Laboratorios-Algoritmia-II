'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

def is_valid_move (x, y, v_size, h_size, mapa):
    return (min(x, y) >= 0) and (x < v_size and y < h_size)

def possible_moves (cx, cy, v_size, h_size, mapa):
    c = []
    if is_valid_move(cx, cy-1, v_size, h_size, mapa) and (mapa[cx][cy] < mapa[cx][cy+1]):
        c.append((mapa[cx][cy],(cx, cy-1)))
    if is_valid_move(cx, cy+1, v_size, h_size, mapa) and (mapa[cx][cy] < mapa[cx][cy-1]):
        c.append((mapa[cx][cy],(cx, cy+1)))
    if is_valid_move(cx+1, cy, v_size, h_size, mapa) and (mapa[cx][cy] < mapa[cx-1][cy]):
        c.append((mapa[cx][cy],(cx+1, cy)))
    if is_valid_move(cx-1, cy, v_size, h_size, mapa) and (mapa[cx][cy] < mapa[cx+1][cy]):
        c.append((mapa[cx][cy],(cx-1, cy)))
    return c

def travessia(mapa):
    v_size = len(mapa)
    h_size = len(mapa[0])
    i = mapa[0][3]
    pi = (0,0)
    vis = {i}
    custo = {pi:0}
    queue = [pi]
    while queue:
        x,y = queue.pop(0)
        for move in possible_moves(x,y,v_size,h_size,mapa):
            if (nx,ny) not in vis:
                vis.add((nx,ny))
                custo[(nx,ny)] = custo[(x,y)] + int(c)
                queue.append((nx,ny))
    return custo



mapa = [
        "4563",
        "9254",
        "7234",
        "3231",
        "3881"
        ]

print("Output: ", travessia(mapa))
print("Solução: " + "(2,10)")
