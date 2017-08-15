
def binary_search(l,r,key):
    if r >l:
        mid =  l + (r-l)//2
        if key > a[mid]:
            return binary_search(mid+1,r,key)
        elif key<a[mid]:
            return binary_search(l, mid-1, key)
        else:
            return mid
    else:
        return -1


if __name__ == '__main__':
    a=[3,10,5,1,2,0,20,5]
    search_eleent=20
    print "index:", binary_search(0,len(a),search_eleent)
