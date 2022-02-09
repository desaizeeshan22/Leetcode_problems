## count occurences of an element in a sorted array
## using binary search to calculate the first and last occurence of an element
## difference in the last and first occurence of the element plus 1(since python is 0 indexed)
## gives the count of element in the array

def bin_first_occurence(arr,l,r,elem):
    while l<=r:
        mid = l + (r - l) // 2
        if arr[mid]==elem:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                r=mid-1
        elif arr[mid]<elem:
            l=mid+1
        else:
            r=mid-1
    return -1

def bin_last_occurence(arr,l,r,elem):
    n=len(arr)-1
    while l<=r:
        mid = l + (r - l) // 2
        if arr[mid]==elem:
            if mid==n or arr[mid+1]!=arr[mid]:
                return mid
            else:
                l=mid+1
        elif arr[mid]<elem:
            l=mid+1
        else:
            r=mid-1
    return -1

def count_occurences(arr,elem):
    if bin_first_occurence(arr,0,len(arr)-1,elem)==1:
        return 0
    return bin_last_occurence(arr,0,len(arr)-1,elem)-bin_first_occurence(arr,0,len(arr)-1,elem)+1
arr=[10,10,20,20,20,30,40,50]
print(count_occurences(arr,50))