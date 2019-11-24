if __name__ == '__main__':
    n, m= input().split(' ')
    
    # print('n: %s, m: %s' %(n, m))
    
    dict1 = []
    dict2 = []
    
    for i in range(int(n)):
        print(i)
        temp_input = str(input())
        dict1.append(temp_input)
    for i in range(int(m)):
        temp_input = str(input())
        dict2.append(temp_input)
    print(dict1)
    print(dict2)
    string1 = ''
    string2 = ''
    
    for j in range(len(dict2)):
    	for i in range(len(dict1)):
    	    
	        if dict1[i] == 'a':
	            string1 = string1 + str(i+1) + ' ' 
	        else:
	            string1 = '-1'
	            break
        
        
    print(string1)
    print(string2)