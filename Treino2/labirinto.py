def is_valid_move (x, y, size, mapa):
	return (min(x, y) >= 0) and (max(x, y) < size) and (mapa[y][x] != '#')

def possible_moves (cx, cy, size, mapa):
	r = []
	c = []
	if is_valid_move(cx, cy-1, size, mapa):
		r.append('N')
		c.append((cx, cy-1))
	if is_valid_move(cx, cy+1, size, mapa):
		r.append('S')
		c.append((cx, cy+1))
	if is_valid_move(cx+1, cy, size, mapa):
		r.append('E')
		c.append((cx+1, cy))
	if is_valid_move(cx-1, cy, size, mapa):
		r.append('O')
		c.append((cx-1, cy))
	return list(zip(r, c))

def caminho(mapa):
	size 	= len(mapa)
	start 	= (0, 0); end = (size-1, size-1)
	visited	= { start }
	queue   = [ start ]
	path    = { start : '' }
	while queue:
		x, y = queue.pop(0)
		if (x, y) == end:
			break
		for move in possible_moves(x, y, size, mapa):
			d, (nx, ny) = move
			if (nx, ny) not in visited:
				visited.add((nx, ny))
				path[(nx, ny)] = path[(x, y)] + d
				queue.append((nx, ny))
	return (path[end])
	