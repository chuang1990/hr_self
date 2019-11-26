# Growing plant
# code war


def growing_plant(upSpeed, downSpeed, desiredHeight):
    #your code here
    day = 0
    current_height = 0
    height_reach = False
    while(not height_reach):
    	current_height = current_height + upSpeed
    	# print(current_height)
    	# print(desiredHeight)
    	day = day + 1	
    	# print(day)
    	if current_height >= desiredHeight:
    		height_reach = True
    	current_height = current_height - downSpeed

    return day

if __name__ == '__main__':
	print("Basic Tests")
	assert growing_plant(100,10,910) == 10, "%d != 10" %growing_plant(100,10,910)
	assert growing_plant(10,9,4) == 1, "%d != 1" %growing_plant(10,9,4)
	assert growing_plant(5,2,0) == 1, "%d != 1" %growing_plant(5,2,0)
	assert growing_plant(5,2,5) == 1, "%d != 1" %growing_plant(5,2,5)
	assert growing_plant(5,2,6) == 2, "%d != 2" %growing_plant(5,2,6)