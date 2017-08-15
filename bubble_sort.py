def bubble_sort(a):
    n=len(a)
    is_swapped = False
    for i in range(n-1):
        k=0
        for j in range(1,n):
            if a[j] < a[k]:
                a[j],a[k]  = a[k],a[j]
                is_swapped = True
            k +=1
        if not is_swapped:
            return a
    return a

if __name__ == '__main__':
    input_data=[2,3,10,5,1,2,0,20,5]
    print bubble_sort(input_data)

