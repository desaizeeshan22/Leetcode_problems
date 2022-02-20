##find a peak element in an array aka an element which is greater than it's immediated
# neighbours on either side eg. input:[5,10,20,15,7] returns 20 since 20>10 and 20>15

def peak(arr):
    n=len(arr)
    if n==1:
        return arr[0]
    ## handling the cases aka the first and last elements only have one neighbour
    if arr[0]>arr[1]:
        return arr[0]
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    # checking from the second to the second last(inclusive element for peak)
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return arr[i]
def optimized_peak(arr):
    n=len(arr)
    lo=0
    hi=n-1
    if n == 1:
        return arr[0]
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if mid==0:
             if arr[mid]>arr[mid+1] :
                 return arr[mid]
        if mid ==n-1:
             if arr[mid] > arr[mid - 1] :
                 return arr[mid]
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]
        elif arr[mid]<=arr[mid-1]:
            hi=mid-1
        else:
            lo=mid+1
    return -1

# arr=[5,10,20,15,7]
# arr=[80,70,60]
# arr=[10,20,15,5,23,90,67]
arr=[5,20,40,30,20,50,60]
print(optimized_peak(arr))
