tests = [
	[[1,2,2,3,3,6,6,9,9], 1],
	[[1,1,2,3,3,6,6,9,9], 2],
	[[1,1,2,2,3,6,6,9,9], 3],
	[[1,1,2,2,3,3,6,9,9], 6],
	[[1,1,2,2,3,3,6,6,9], 9],

	[[0,1,1,2,2,3,3,6,6,9,9], 0],
	[[0,0,1,2,2,3,3,6,6,9,9], 1],
	[[0,0,1,1,2,3,3,6,6,9,9], 2],
	[[0,0,1,1,2,2,3,6,6,9,9], 3],
	[[0,0,1,1,2,2,3,3,6,9,9], 6],
	[[0,0,1,1,2,2,3,3,6,6,9], 9],
]


def bs(l:list, s:int=None, e:int=None):
	if s is None:
		s = 0
	if e is None:
		e = len(l)-1

	while s < e:
		mid = (s + e) // 2

		if mid % 2 == 0 and l[mid] == l[mid + 1]:
			s = mid + 2
		elif mid % 2 == 1 and l[mid] == l[mid - 1]:
			s = mid + 1
		else:
			e = mid
	
	return l[s]




for test, answer in tests:
	res = bs(test)
	print(res)
	assert res == answer
