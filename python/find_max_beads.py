# find max beads of an array of necklaces
# given an array, the index is the number of beads and the element is the number to the next bead
# if given empty array, return 0
#

'''
main function
input: A - an array containing information of the necklaces
output: the maximum number of connected beads in A
'''
def main(A):
	# print(A)
	if len(A) < 1:
		return 0
	elif len(A) == 1:
		return 1 if A[0] == 0 else 0
	else:
		max_found = 0
		temp_array = []
		keep_searching = True
		# print("original A: ", A)
		update_A = A
		counter = 0
		while(True):  
			if not update_A:
				keep_searching = False
				break
			# print("counter %d" % counter)
			# print("A passed into find_beads")
			temp = find_beads(counter, A, temp_array)
			# print("one necklace: ", temp)
			if len(temp) > max_found:
				max_found = len(temp)
			# print("max_found %d, temp length: %d" %(max_found, len(temp)))
			update_A = [x for x in update_A if x not in temp]
			# print("updated A: ", update_A)
			counter += 1
			temp_array = []
		return max_found

def find_beads(index, array, temp_array):
	temp_array.append(index)
	if array[index] in temp_array:
		return temp_array
	return find_beads(array[index], array, temp_array)


if __name__ == '__main__':
	answers = [4, 0, 1]
	arrays = [[3, 1, 4, 0, 5, 7, 6, 2], [], [0, 1, 2]]
	for a in range(len(arrays)):
		print(arrays[a])
		maxbeads = main(arrays[a])
		assert maxbeads == answers[a], "maxbeads = %d, answer = %d" %(maxbeads, answers[a])
		print("maxbeads = %d, answer = %d" %(maxbeads, answers[a]))