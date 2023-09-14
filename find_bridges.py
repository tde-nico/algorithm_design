# find bridges O(V+E)

G = {
	'0': ['1'],
	'1': ['2'],
	'2': ['0', '3', '5'],
	'3': ['4'],
	'4': [],
	'5': ['6'],
	'6': ['7'],
	'7': ['8'],
	'8': ['5'],
}




def find_bridges(g:dict):
	ID = [0]
	ids = {node: 0 for node in g.keys()}
	low = {node: 0 for node in g.keys()}
	visited = set()
	bridges = []

	def _dfs(at, parent):
		visited.add(at)
		ID[0] += 1
		low[at] = ids[at] = ID[0]

		for to in g[at]:
			if to == parent:
				continue
			if to not in visited:
				_dfs(to, at)
				low[at] = min(low[at], low[to])
				if ids[at] < low[to]:
					bridges.append(at + '_' + to)
			else:
				low[at] = min(low[at], ids[to])


	for node in g.keys():
		if node not in visited:
			_dfs(node, '-1')
	return bridges



if __name__ == '__main__':
	bridges = find_bridges(G)
	print(bridges)
