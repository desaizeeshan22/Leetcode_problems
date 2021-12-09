def iter_binary_search(arr,left,right,value):
    while left<=right:
        mid=(left+right)//2
        if value==arr[mid]:
            return mid
        elif value>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1

a=[1,2,3,4,5]
print(iter_binary_search(a,0,len(a),5))
