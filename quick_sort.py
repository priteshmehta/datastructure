def partition(a,part_start,part_end):
    i = part_start -1
    pivot = a[part_end]    
    for j in range(part_start,part_end-1):        
        if a[j] <= pivot:
            i += 1
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[i+1]
    a[i+1] = pivot
    a[part_end] = tmp
    return i+1

def quick_sort(b,part_start,part_end):
    if part_start < part_end:
        pivot_index = partition(b,part_start,part_end)        
        quick_sort(a,part_start,pivot_index-1)
        quick_sort(a,pivot_index+1,part_end)

if __name__ == '__main__':
    a=[2,3,10,5,1,2,0,20,5]
    quick_sort(a,0,len(a)-1)
    print a
