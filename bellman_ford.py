# bellman ford O(E*V)

G1 = {
	'0': [('1', 1), ('2', 1)],
	'1': [('3', 4)],
	'2': [('1', 1)],
	'3': [('2', -6), ('4', 1), ('5', 1)],
	'4': [('5', 1), ('6', 1)],
	'5': [('6', 1)],
	'6': [],
}

G2 = {
	'0': [('1', 5)],
	'1': [('2', 20), ('5', 30), ('6', 60)],
	'2': [('3', 10), ('4', 75)],
	'3': [('2', -15)],
	'4': [('9', 100)],
	'5': [('4', 25), ('6', 5), ('8', 50)],
	'6': [('7', -50)],
	'7': [('8', -10)],
	'8': [],
	'9': [],
}

def bellman_ford(g:dict, start:str=None):
	if start == None:
		start = list(g.keys())[0]
	dist = {node: 1e30 for node in g.keys()}
	dist[start] = 0
	v = sum([len(edges) for edges in g.values()])
	for _ in range(v):
		for edge in g.keys():
			for to, cost in g[edge]:
				if dist[edge] + cost < dist[to]:
					dist[to] = dist[edge] + cost
	for edge in g.keys():
		for to, cost in g[edge]:
			if dist[edge] + cost < dist[to]:
				dist[to] = -1e30
	return dist



if __name__ == '__main__':
	res = bellman_ford(G1)
	print(res)
	res = bellman_ford(G2)
	print(res)
