# find articulations O(V+E)

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




def find_articulations(g:dict):
	ID = [0]
	OUT_EDGE_COUNT = [0]
	ids = {node: 0 for node in g.keys()}
	low = {node: 0 for node in g.keys()}
	is_art = {node: False for node in g.keys()}
	visited = set()

	def _dfs(root, at, parent):
		if parent == root:
			OUT_EDGE_COUNT[0] += 1
		visited.add(at)
		ID[0] += 1
		low[at] = ids[at] = ID[0]

		for to in g[at]:
			if to == parent:
				continue
			if to not in visited:
				_dfs(root, to, at)
				low[at] = min(low[at], low[to])
				if ids[at] <= low[to]:
					is_art[at] = True
			else:
				low[at] = min(low[at], ids[to])


	for node in g.keys():
		if node not in visited:
			OUT_EDGE_COUNT[0] = 0
			_dfs(node, node, '-1')
			is_art[node] = OUT_EDGE_COUNT[0] > 1
	return is_art



if __name__ == '__main__':
	articulations = find_articulations(G)
	print(articulations)
