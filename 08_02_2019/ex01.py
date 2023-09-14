'''
give the python code that from a graph G non direct and weigthed, returns a max spanning tree:
'''

# O(E*log(E))

NO = None
G = [# 0   1   2   3   4   5   6
	[ NO, +9, +0, +5, NO, +7, NO ], # 0
	[ +9, NO, NO, -2, +3, NO, +4 ], # 1
	[ +0, NO, NO, NO, NO, +6, NO ], # 2
	[ +5, -2, NO, NO, NO, +2, +3 ], # 3
	[ NO, +3, NO, NO, NO, NO, +6 ], # 4
	[ +7, NO, +6, +2, NO, NO, +1 ], # 5
	[ NO, +4, NO, +3, +6, +1, NO ], # 6
]


def kruskal_max(g:list, start:int=None):
	if start is None:
		start = 0
	mst_cost = 0
	mst_edges = []
	parent = []
	rank = []
	m = 0
	i = 0
	V = [
		[at, to, cost]
		for at, row in enumerate(g)
		for to, cost in enumerate(row)
		if cost is not NO
	]
	sort = sorted(V, key=lambda x:x[2], reverse=True)


	def _find(parent, i):
		if parent[i] == i:
			return i
		return _find(parent, parent[i])


	def _apply_union(parent, rank, x, y):
		xroot = _find(parent, x)
		yroot = _find(parent, y)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1


	for node in range(len(g)):
		parent.append(node)
		rank.append(0)
	
	while m < len(g) - 1:
		at, to, cost = sort[i]
		i += 1
		x = _find(parent, at)
		y = _find(parent, to)
		if x != y:
			m += 1
			mst_edges.append([at, to, cost])
			mst_cost += cost
			_apply_union(parent, rank, x, y)
	
	return mst_cost, mst_edges



if __name__ == '__main__':
	mst_cost, mst_edges = kruskal_max(G)
	print(mst_cost, mst_edges)
