def binary_search_last_occ(arr,l,r,elem):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid]==elem:
        if mid==len(arr)-1 or arr[mid]!=arr[mid+1]:
            return mid
        else:
            return binary_search_last_occ(arr,mid+1,r,elem)
    elif arr[mid]<elem:
        return binary_search_last_occ(arr,mid+1,r,elem)
    else:
        return binary_search_last_occ(arr,l,mid-1,elem)

arr=[40,30,10,10,10,20,20,20,50]
n=len(arr)-1
arr.sort()
print(binary_search_last_occ(arr,0,n,20))
print(binary_search_last_occ(arr,0,n,10))
print(binary_search_last_occ(arr,0,n,25))