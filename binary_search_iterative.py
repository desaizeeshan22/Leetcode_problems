def binary_search(arr,elem):
    l=0
    r=len(arr)-1
    arr.sort()
    while l<=r:
        m = int((l + r) / 2)
        if arr[m]==elem:
            return m
        elif arr[m]<elem:
            l=m+1
        else:
            r=m-1
    return -1
arr=[40,30,10,20,50]
print(binary_search(arr,50))
print(binary_search(arr,5))