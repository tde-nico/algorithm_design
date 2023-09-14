'''
a pawn is placed at (1,1) in a NxN chessboard and with a sequence of moves it should reach (N,N),
it can go from a spot (i,j) to (i+1,j) or (i,j+1) with i <= n and j <= n, if there are red and blue spots,
create a python algo with O(n^2) time complexity that computes the red paths from (1,1) to (n,n).
'''


G = [
	[0, 0, 0, 0],
	[0, -1, 0, 0],
	[0, 0, -1, 0],
	[0, 0, 0, 0],
]


def count_blue_paths(g: list):
	n = len(g)
	dp = [g[i].copy() for i in range(n)]
	dp[0][0] = 1

	for y in range(n):
		for x in range(n):
			if dp[y][x] != -1:
				if x > 0 and dp[y][x - 1] != -1:
					dp[y][x] += dp[y][x - 1]
				if y > 0 and dp[y - 1][x] != -1:
					dp[y][x] += dp[y - 1][x]
	
	print(dp)
	return dp[n - 1][n - 1]
	


if __name__ == '__main__':
	count = count_blue_paths(G)
	print(count)


