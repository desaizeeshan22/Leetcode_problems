# Taking an input number K and an array with numbers ranging from 0 to K-1
# K=5
# arr=[1,4,4,0,1]
# return sorted array aka in this example =[0,1,1,4,4]

def counting_sort(arr,K):
    counts=[0]*K ## creating an array holding the counts of elements in their respective indices
    # aka if there are three 1's the index of 1 is 3 in the array
    for elem in arr:
        counts[elem]+=1
    for i in range(1,len(counts)):
        counts[i]+=counts[i-1] ## count array contains the number of elements less than equal to the index value of
        ##count
    result=[0]*len(arr) ## array to store the sorted result
    for elem in arr:
        if counts[elem]>=1:
            result[counts[elem]-1]=elem
            counts[elem]-=1
    return result

print(counting_sort([1,4,4,0,1],5))