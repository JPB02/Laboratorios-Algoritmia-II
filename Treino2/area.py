def is_valid_move (x, y, size, mapa):
	return (min(x, y) >= 0) and (max(x, y) < size) and (mapa[y][x] != '*')

def possible_moves(x, y, size, mapa):
	moves = []
	if is_valid_move(x, y-1, size, mapa):
		moves.append((x, y-1))
	if is_valid_move(x, y+1, size, mapa):
		moves.append((x, y+1))
	if is_valid_move(x+1, y, size, mapa):
		moves.append((x+1, y))
	if is_valid_move(x-1, y, size, mapa):
		moves.append((x-1, y))
	return moves

def area(p,mapa):
	size = len(mapa)
	map_area = 1
	vis = {p}
	queue = [p]
	while queue:
		x,y = queue.pop(0)
		for move in possible_moves(x,y,size,mapa):
			nx,ny = move
			if (nx,ny) not in vis:
				vis.add((nx,ny))
				map_area += 1
				queue.append((nx,ny))
	return map_area
