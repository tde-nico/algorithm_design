# topological sort O(V+E)

from dfs import dfs, dfs_weigthed

G = {
	'a': ['d'],
	'b': ['d'],
	'c': ['a', 'b'],
	'd': ['g', 'h'],
	'e': ['a', 'd', 'f'],
	'f': ['j', 'k'],
	'g': ['i'],
	'h': ['i', 'j'],
	'i': ['l'],
	'j': ['l', 'm'],
	'k': ['j'],
	'l': [],
	'm': [],
}

def topsort(g: dict):
	order = []
	visited = set()
	for at in g.keys():
		if at not in visited:
			vnodes = dfs(g, visited, at)
			for node in vnodes:
				order.insert(0, node)
	return order


def topsort_weigthed(g: dict):
	order = []
	visited = set()
	for at in g.keys():
		if at not in visited:
			vnodes = dfs_weigthed(g, visited, at)
			for node in vnodes:
				order.insert(0, node)
	return order


if __name__ == '__main__':
	order = topsort(G)
	print(order)
