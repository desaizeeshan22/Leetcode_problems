def recursive_binary_search(arr,value,low,high):
    if low>high:
        return -1
    mid=int((low+high)/2)
    if value==arr[mid]:
        return mid
    if value<arr[mid]:
        return recursive_binary_search(arr,value,low,mid-1)
    return recursive_binary_search(arr,value,mid+1,high)


a=[1,2,3,4,5]
print(recursive_binary_search(a,3,0,len(a)))


