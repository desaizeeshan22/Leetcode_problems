def hoares_partition(arr,l,r):
    i=l+1
    j=r
    pivot=arr[l]
    while True:
        while i<=j and arr[i]<=pivot:
           i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[l],arr[j]=arr[j],arr[l]
    return j




def lomuto_partition(arr,l,r):
    pivot=arr[r]
    i=l-1
    for j in range(l,r):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def quicksort(arr,l,r):
    if l<r:
        pivot=lomuto_partition(arr,l,r)
        quicksort(arr,l,pivot-1)
        quicksort(arr,pivot+1,r)
def quicksort_hoares(arr,l,r):
    if l<r:
        pivot=hoares_partition(arr,l,r)
        quicksort_hoares(arr,l,pivot)
        quicksort_hoares(arr,pivot+1,r)
        

arr=[40,20,50,10,30]
quicksort(arr,0,len(arr)-1)
# print(hoares_partition(arr,0,len(arr)-1))
# quicksort_hoares(arr,0,len(arr)-1)
print(arr)