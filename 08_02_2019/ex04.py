'''
given a white horse on the spot (x1, y1) in a NxN chessboard, with a set of moves it should reach the spot (x2, y2),
an horse can do the following moves starting from (i, j): (i+1,j+2), (i+1,j-2), (i-1,j+2), (i-1,j-2), (i+2,j+1), (i+2,j-1), (i-2,j+1), (i-2,j-1).
write a python algo that determinate is exists a list of moves from (x1,y1) to (x2,y2), and if yes returns tha minimum amount of moves.
'''


def horse_moves(n:int, x1:int, y1:int, x2:int, y2:int):
	moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
	valid = lambda n,x,y: x >= 0 and y >= 0 and x <= n and y <= n
	visited = set()
	queue = [(x1,y1,0)]
	visited.add((x1, y1))

	while queue:
		curr_x, curr_y, cost = queue.pop(0)

		if curr_x == x2 and curr_y == y2:
			return cost

		for dx, dy in moves:
			new_x, new_y = curr_x + dx, curr_y + dy
			if valid(n, new_x, new_y) and (new_x, new_y) not in visited:
				visited.add((new_x, new_y))
				queue.append((new_x, new_y, cost + 1))
	
	return -1



if __name__ == '__main__':
	N = 8
	x1, y1 = 0, 0
	x2, y2 = 7, 7

	moves = horse_moves(N, x1, y1, x2, y2)
	print(moves)
