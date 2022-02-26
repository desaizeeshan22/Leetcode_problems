def longest_sub_array_given_sum(arr,k):
    max_len=0
    for i in range(len(arr)):
        sum_=0
        for j in range(i,len(arr)):
            sum_+=arr[j]
            if sum_==k:
                max_len=max(j-i+1,max_len)
    return max_len
def long_sub_array_efficient(arr,k):
    hash_map={0:0}
    sum_=0
    max_len=0
    for i in range(len(arr)):
        sum_+=arr[i]
        if sum_ == k:
            max_len = i + 1
        if  sum_-k in hash_map:
            max_len=max(i+1-hash_map[sum_-k],max_len)
        elif sum_ not in hash_map:
            hash_map[sum_] = i + 1
    return max_len
print("efficient  "+str(long_sub_array_efficient([5,8,-4,-4,9,-2,2],0)))
print(longest_sub_array_given_sum([5,8,-4,-4,9,-2,2],0))
print("efficient "+str(long_sub_array_efficient([3,1,0,1,8,2,3,6],5)))
print(longest_sub_array_given_sum([3,1,0,1,8,2,3,6],5))
print("efficient "+str(long_sub_array_efficient([8,3,7],0)))
print(longest_sub_array_given_sum([8,3,7],0))
print(long_sub_array_efficient([-1,1,-1,1],0))