def selection_sort(a):
    n = len(a)
    for i in range(n):
        max_index = 0
        for j in range(n-i):
            if a[max_index] < a[j]:
                max_index = j

        #swap max number
        a[max_index],a[j] = a[j],a[max_index]
    return a

if __name__ == '__main__':
	input_data=[2,3,10,5,1,2,0,20,5]
	print selection_sort(input_data)