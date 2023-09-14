# BFS O(V+E)

G = [
	#0,1,2,3,4,5,6,7,8,9,0,1,2
	[0,0,0,0,0,0,0,1,0,1,0,1,0],#0
	[0,0,0,0,0,0,0,0,1,0,1,0,0],#1
	[0,0,0,1,0,0,0,0,0,0,0,0,1],#2
	[0,0,1,0,1,0,0,1,0,0,0,0,0],#3
	[0,0,0,1,0,0,0,0,0,0,0,0,0],#4
	[0,0,0,0,0,0,1,0,0,0,0,0,0],#5
	[0,0,0,0,0,1,0,1,0,0,0,0,0],#6
	[1,0,0,1,0,0,1,0,0,0,0,1,0],#7
	[0,1,0,0,0,0,0,0,0,1,0,0,1],#8
	[1,0,0,0,0,0,0,0,1,0,1,0,0],#9
	[0,1,0,0,0,0,0,0,0,1,0,0,0],#0
	[1,0,0,0,0,0,0,1,0,0,0,0,0],#1
	[0,0,1,0,0,0,0,0,1,0,0,0,0],#2
]

def bfs(g:list,at:int=0):
	visited = set()
	queue = [at]
	visited.add(at)
	vnodes = []
	while queue:
		node = queue.pop(0)
		# print(node)
		vnodes += [node]
		for i, neighbour in enumerate(g[node]):
			if neighbour and i not in visited:
				visited.add(i)
				queue.append(i)
	return vnodes


if __name__ == '__main__':
	vnodes = bfs(G)
	print(vnodes)
