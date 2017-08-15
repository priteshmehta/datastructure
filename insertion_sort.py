def insertion_sort(a):
    n = len(a)
    k = 0
    for i in range(n):
        start_element = a[i]
        hole_indx = i
        while hole_indx > 0 and a[hole_indx-1] > start_element:
            a[hole_indx] = a[hole_indx-1]
            hole_indx -=1
        a[hole_indx] = start_element
    return a

if __name__ == '__main__':
    input_data=[2,3,10,5,1,2,0,20,5]
    print insertion_sort(input_data)
