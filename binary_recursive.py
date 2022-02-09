def binary_search(arr,l,r,elem):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid]==elem:
        return mid
    elif arr[mid]<elem:
        return binary_search(arr,mid+1,r,elem)
    else:
        return binary_search(arr,l,mid-1,elem)

arr=[40,30,10,20,50]
n=len(arr)-1
arr.sort()
print(binary_search(arr,0,n,50))
print(binary_search(arr,0,n,10))
print(binary_search(arr,0,n,20))