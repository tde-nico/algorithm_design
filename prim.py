# Lazy Prim O(E*log(E))
# Eager Prim O(E*log(V))

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
# MST = 9 [ 0-2 0-3 3-1 1-4 3-5 5-6 ]


class PriorityQueue():
	def __init__(self):
		self.queue = []
	
	def empty(self):
		if len(self.queue):
			return False
		return True

	def put(self, item):
		self.queue.append(item)

	def poll(self):
		polled = self.queue[0]
		index = 0
		for i in range(1, len(self.queue)):
			if polled[2] > self.queue[i][2]:
				polled = self.queue[i]
				index = i
		self.queue.pop(index)
		return polled



class EagerPQ(PriorityQueue):
	def put(self, item):
		for i in range(len(self.queue)):
			if self.queue[i][1] == item[1]:
				if self.queue[i][2] > item[2]:
					self.queue[i] = item
				break
		else:
			self.queue.append(item)



def lazy_prim(g:list, start:int=None):
	if start == None:
		start = 0
	visited = set()
	pq = PriorityQueue()
	m = len(g) - 1
	edge_count = 0
	mst_cost = 0
	mst_edges = [None] * m

	def _add_edges(to):
		visited.add(to)
		for neighbour, new_cost in enumerate(g[to]):
			if new_cost is NO:
				continue
			if neighbour not in visited:
				pq.put([to, neighbour, new_cost])

	_add_edges(start)

	while not pq.empty() and edge_count != m:
		edge = pq.poll()
		to = edge[1]
		cost = edge[2]

		if to in visited:
			continue
		
		mst_edges[edge_count] = edge
		mst_cost += cost
		edge_count += 1

		_add_edges(to)

	if edge_count != m:
		return None, None
	return mst_cost, mst_edges



def eager_prim(g:list, start:int=None):
	if start == None:
		start = 0
	visited = set()
	pq = EagerPQ()
	m = len(g) - 1
	edge_count = 0
	mst_cost = 0
	mst_edges = [None] * m

	def _add_edges(to):
		visited.add(to)
		for neighbour, new_cost in enumerate(g[to]):
			if new_cost is NO:
				continue
			if neighbour not in visited:
				pq.put([to, neighbour, new_cost])

	_add_edges(start)

	while not pq.empty() and edge_count != m:
		edge = pq.poll()
		to = edge[1]
		cost = edge[2]

		if to in visited:
			continue
		
		mst_edges[edge_count] = edge
		mst_cost += cost
		edge_count += 1

		_add_edges(to)

	if edge_count != m:
		return None, None
	return mst_cost, mst_edges



if __name__ == '__main__':
	mst_cost, mst_edges = lazy_prim(G)
	print(mst_cost, mst_edges)
	mst_cost, mst_edges = eager_prim(G)
	print(mst_cost, mst_edges)

