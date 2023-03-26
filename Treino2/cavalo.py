def aux(x,y):
    new_pos = []
    x_pos=[-1,1,-2,-2,2,2,1,-1]
    y_pos=[2,2,1,-1,1,-1,-2,-2]
    for i in range(8):
        new_pos.append((x+x_pos[i], y+y_pos[i]))
    return new_pos
        

def saltos(o,d):
    count = 0
    dist={o:0}
    vis={o}
    queue = [o]
    while queue:
        x,y = queue.pop(0)
        if (x,y) == d:
            break
        for mov in aux(x,y):
            if mov not in vis:
                vis.add(mov)
                dist[mov] = dist[(x,y)]+1
                queue.append(mov)
    return dist[d]
