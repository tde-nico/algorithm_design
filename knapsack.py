# knapsack (0/1) O(n*W)

CAPACITY = 7
W = [3, 1, 3, 2, 4]
V = [2, 2, 4, 3, 5]


def knapsack(capacity: int, w: list, v: list):
	if capacity < 0 or w is None or v is None or len(w) != len(w):
		raise Exception("Invalid Arguments")
	n = len(w)
	dp = [[0] * (capacity + 1) for _ in range(n + 1)]

	for i in range(n):
		w_curr, v_curr = w[i], v[i]
		for size in range(capacity):
			dp[i + 1][size + 1] = dp[i][size + 1]
			if (size+1) >= w_curr and (dp[i][size+1-w_curr] + v_curr) > dp[i+1][size+1]:
				dp[i + 1][size + 1] = dp[i][size + 1 - w_curr] + v_curr
	
	size = capacity
	selected = []

	for i in range(n, 0, -1):
		if dp[i][size] != dp[i - 1][size]:
			selected.append(i - 1)
			size -= w[i - 1]

	return dp[n][capacity], selected[::-1]


if __name__ == '__main__':
	max_value, selected = knapsack(CAPACITY, W, V)
	print(max_value, selected)
