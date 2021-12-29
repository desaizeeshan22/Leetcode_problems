## calculate sum of elements from start index to end index of an array
##[start,end] inclusive


def partial_sum(arr):## calculates sum upto each index of an array
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]
    partial_sum_arr=[0]*n
    partial_sum_arr[0]=arr[0]
    partial_sum_arr[1]=arr[0]+arr[1]
    for i in range(2,n):
        partial_sum_arr[i]=partial_sum_arr[i-1]+arr[i]
    return partial_sum_arr
def query(arr,start,end):## calculates sum of elements from start index to end index of an array
    partial_sum_list=partial_sum(arr)
    return partial_sum_list[end]-partial_sum_list[start-1]
print(partial_sum([7,-2,3,9,-11,5,1,-3]))
print(query([7,-2,3,9,-11,5,1,-3],2,4))