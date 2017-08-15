
if __name__ == '__main__':
	a=[1,0,0,1,1,0,1,1,0,0]
	i=0
	j=len(a)-1
	while(i<j):
	    if a[i] == 0:
	        i+=1
	    elif a[j] == 1:
	        j -= 1
	    else:
	        a[i] = 0
	        a[j] = 1
	        i+=1
	        j-=1
	print a
