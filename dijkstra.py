# Dijkstra O(E*log(V))
# Dijkstra D-ary Heap O(E*log(E/V)(V))
# Dijkstra Fibonacci Heap O(E+V*log(V))

G = {
    '0': [('1', 4), ('2', 1)],
    '1': [('3', 1)],
    '2': [('1', 2), ('3', 5)],
    '3': [('4', 3)],
    '4': [],
}

class PriorityQueue():
	def __init__(self):
		self.q = []
	
	def empty(self):
		if len(self.q):
			return False
		return True

	def put(self, item):
		self.q.append(item)

	def poll(self):
		polled = self.q[0]
		index = 0
		for i in range(1, len(self.q)):
			if polled[1] > self.q[i][1]:
				polled = self.q[i]
				index = i
		self.q.pop(index)
		return polled


def dijkstra(g:dict, start:str=None):
	if start == None:
		start = list(g.keys())[0]
	visited = set()
	prev = {node: None for node in g.keys()}
	dist = {node: 1e30 for node in g.keys()}
	dist[start] = 0
	pq = PriorityQueue()
	pq.put((start, 0))
	while not pq.empty():
		node, cost = pq.poll()
		visited.add(node)
		if dist[node] < cost:
			continue
		for neighbour in g[node]:
			if neighbour[0] in visited:
				continue
			new_dist = dist[node] + neighbour[1]
			if new_dist < dist[neighbour[0]]:
				dist[neighbour[0]] = new_dist
				prev[neighbour[0]] = node
				pq.put((neighbour[0], new_dist))
	return dist, prev


def find_shortest_path(g:dict, start:str, end:str):
	dist, prev = dijkstra(g, start)
	path = []
	if dist[end] == 1e30:
		return path
	at = end
	while at != None:
		path.append(at)
		at = prev[at]
	return path[::-1]


if __name__ == '__main__':
    dist, prev = dijkstra(G)
    print(dist)
    print(prev)
    short_path = find_shortest_path(G, '0', '4')
    print(short_path)
    
