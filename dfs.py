# DFS O(V+E)

G = {
	'0': ['9'],
	'1': ['0'],
	'2': [],
	'3': ['2', '4', '5'],
	'4': [],
	'5': ['6'],
	'6': ['7'],
	'7': ['3', '10'],
	'8': ['1', '7'],
	'9': ['8'],
	'10': ['11'],
	'11': ['7'],
	'12': [],
}


def	dfs(g:dict, visited:set=None, at:str=None):
	if visited == None:
		visited = set()
	if at == None:
		at = list(g.keys())[0]
	if at in visited:
		return []
	visited.add(at)
	# print(at)
	vnodes = [at]
	for neighbour in g[at]:
		vnodes += dfs(g, visited, neighbour)
	return vnodes


def	dfs_weigthed(g:dict, visited:set=None, at:str=None):
	if visited == None:
		visited = set()
	if at == None:
		at = list(g.keys())[0]
	if at in visited:
		return []
	visited.add(at)
	# print(at)
	vnodes = [at]
	for neighbour in g[at]:
		vnodes += dfs_weigthed(g, visited, neighbour[0])
	return vnodes


if __name__ == '__main__':
	visited = set()
	vnodes = dfs(G, visited)
	print(vnodes)
	print(visited)
