# floyd warshall O(V**3)

G = [
	#0,1,2,3,4,5,6,7,8,9,0,1,2
	[0,0,0,0,0,0,0,1,0,2,0,3,0],#0
	[0,0,0,0,0,0,0,0,1,0,1,0,0],#1
	[0,0,0,4,0,0,0,0,0,0,0,0,3],#2
	[0,0,4,0,1,0,0,1,0,0,0,0,0],#3
	[0,0,0,1,0,0,0,0,0,0,0,0,0],#4
	[0,0,0,0,0,0,7,0,0,0,0,0,0],#5
	[0,0,0,0,0,7,0,6,0,0,0,0,0],#6
	[1,0,0,1,0,0,6,0,0,0,0,1,0],#7
	[0,1,0,0,0,0,0,0,0,1,0,0,1],#8
	[2,0,0,0,0,0,0,0,1,0,2,0,0],#9
	[0,1,0,0,0,0,0,0,0,1,0,0,0],#0
	[3,0,0,0,0,0,0,2,0,0,0,0,0],#1
	[0,0,3,0,0,0,0,0,1,0,0,0,0],#2
]

def floyd_warshall(g:list):
	n = len(g)

	# setup
	dp = [[1e30] * n for _ in range(n)]
	nxt = [[1e30] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			dp[i][j] = g[i][j]
			if g[i][j] != 1e30:
				nxt[i][j] = j

	# shortest path algorithm
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dp[i][k] + dp[k][j] < dp[i][j]:
					dp[i][j] = dp[i][k] + dp[k][j]
					nxt[i][j] = nxt[i][k]
	
	# propagate negative cycles
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dp[i][k] + dp[k][j] < dp[i][j]:
					dp[i][j] = -1e30
					nxt[i][j] = -1

	return dp, nxt


def recunstruct_path(dp:list, nxt:list, start:int, end:int):
	path = []
	if dp[start][end] == 1e30:
		return path
	at = start
	while at != end:
		if at == -1:
			return None
		path.append(at)
		at = nxt[at][end]
	if nxt[at][end] == -1:
		return None
	path.append(end)
	return path



if __name__ == '__main__':
	from pprint import pprint
	for i in range(len(G)):
		for j in range(len(G)):
			if not G[i][j]:
				G[i][j] = 1e30
	dp, nxt = floyd_warshall(G)
	pprint(dp)
	pprint(nxt)
	path = recunstruct_path(dp, nxt, 0, 4)
	print(path)
