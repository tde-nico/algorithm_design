# single source shortest path O(V+E)

from topsort import topsort_weigthed

G = {
	'a': [('b', 3), ('c', 6)],
	'b': [('c', 4), ('d', 4), ('e', 11)],
	'c': [('d', 8), ('g', 11)],
	'd': [('e', -4), ('f', 5), ('g', 2)],
	'e': [('h', 9)],
	'f': [('h', 1)],
	'g': [('h', 2)],
	'h': [],
}

def sssp(g:dict, at:str=None):
	if at == None:
		at = list(g.keys())[0]
	dist = {node: 1e30 for node in g.keys()}
	top = topsort_weigthed(g)[::-1]
	dist[at] = 0
	for node in top:
		if dist[node] != 1e30:
			for neighbour in g[node]:
				new_dist = dist[node] + neighbour[1]
				if dist[neighbour[0]] == 1e30:
					dist[neighbour[0]] = new_dist
				else:
					dist[neighbour[0]] = min(dist[neighbour[0]], new_dist)
	return dist


def sssp_long(g:dict, at:str=None):
	if at == None:
		at = list(g.keys())[0]
	g = {key: [[v[0], v[1] * -1] for v in item] for key, item in g.items()}
	dist = {node: 1e30 for node in g.keys()}
	top = topsort_weigthed(g)[::-1]
	dist[at] = 0
	for node in top:
		if dist[node] != 1e30:
			for neighbour in g[node]:
				new_dist = dist[node] + neighbour[1]
				if dist[neighbour[0]] == 1e30:
					dist[neighbour[0]] = new_dist
				else:
					dist[neighbour[0]] = min(dist[neighbour[0]], new_dist)
	dist = {key: -value for key, value in dist.items()}
	return dist


if __name__ == '__main__':
	dist = sssp(G)
	print(dist)
	dist_long = sssp_long(G)
	print(dist_long)
