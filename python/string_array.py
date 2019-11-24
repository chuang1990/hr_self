def string_to_array(s):
	print(s)
	if s == None:
		return [""]
	else:
		array = s.split(" ")
		print(array)
		return array
    # your code here

if __name__ == '__main__':
	# string_to_array()
	assert string_to_array("Robin Singh") == ["Robin", "Singh"]
	assert string_to_array("CodeWars") == ["CodeWars"]
	assert string_to_array("I love arrays they are my favorite") == ["I", "love", "arrays", "they", "are", "my", "favorite"]
	assert string_to_array("1 2 3") == ["1", "2", "3"]
	assert string_to_array("") == [""]