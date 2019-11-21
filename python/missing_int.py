'''
find the missing positive integer
give an array of N numbers find the first missing positive int(> 0)
ex. [392, 4] returns 1, [1,2,3,4] returns 5, [-1,-2] returns 1, [0] returns 1
N is in range (1, 100000)
element values range from (-100000000, 100000000)
'''

def main(a):

	return 1

if __name__ == '__main__':
	answers = [1, 1, 1, 1, 4]
	arrays = [[0],[4,3,2],[1111111,39402,-30219,-1], [-1,-2,-3,-10000],[1,2,3]]
	for a in range(len(arrays)):
		print(arrays[a])
		first_missing_int = main(arrays[a])
		print(first_missing_int)
		assert first_missing_int == answers[a], "found int: %d, answer: %d" %(first_missing_int, answers[a])