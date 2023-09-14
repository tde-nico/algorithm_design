# Tarjan O(V+E)

G = {
	'0': ['1'],
	'1': ['2', '3', '4'],
	'2': ['0', '4'],
	'3': ['5'],
	'4': ['5'],
	'5': ['4'],
}


def tarjan(g:dict):
	UNVISITED = -1
	ID = [0]
	SCC_COUNT = [0]
	ids = {node: 0 for node in g.keys()}
	low = {node: 0 for node in g.keys()}
	on_stack = {node: False for node in g.keys()}
	stack = []


	def _dfs(at):
		stack.append(at)
		on_stack[at] = True
		ids[at] = low[at] = ID[0]
		ID[0] += 1

		for to in g[at]:
			if ids[to] == UNVISITED:
				_dfs(to)
			if on_stack[to]:
				low[at] = min(low[at], low[to])
		
		if ids[at] == low[at]:
			while node := stack.pop(-1):
				on_stack[node] = False
				low[node] = ids[at]
				if node == at:
					break
			SCC_COUNT[0] += 1


	for node in g.keys():
		ids[node] = UNVISITED
	for node in g.keys():
		if ids[node] == UNVISITED:
			_dfs(node)

	return low



if __name__ == '__main__':
	scc_components = tarjan(G)
	print(scc_components)
