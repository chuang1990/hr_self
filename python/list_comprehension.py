# list_comprehension.py
'''
x = int ( raw_input()) 
y = int ( raw_input()) 
n = int ( raw_input()) 
ar = [] 
p = 0 
for i in range ( x + 1 ) : 
    for j in range( y + 1): 
        if i+j != n: ar.append([]) 
        ar[p] = [ i , j ] 
        p+=1 print ar

x = int ( raw_input()) 
y = int ( raw_input()) 
n = int ( raw_input()) 
print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i+j+k) != n)])