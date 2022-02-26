##count distinct elements in contiguous windows of size k for a given array arr
# eg arr=[10, 20, 20, 10, 30, 40, 10],k=4 ans=[2,3,4,3]
from collections import Counter
def window(arr, k):
    res = []
    for i in range(0, len(arr) - k + 1):
        hash_map = {}
        count = 0
        for j in range(i, i + k):
            if arr[j] not in hash_map:
                count += 1
                hash_map[arr[j]] = 1
            else:
                hash_map[arr[j]] += 1
        res.append(count)
    return res


def naive(arr, k):
    res = []
    for i in range(0, len(arr) - k + 1):
        count = 0
        for j in range(i, i + k):
            flag = False
            for p in range(i, j):
                if arr[p] == arr[j]:
                    flag = True
                    break
            if not flag:
                count += 1
        res.append(count)
    return res
def eff_window(arr,k):
    res=[]
    first_k=Counter(arr[:k])
    res.append(len(first_k))
    for i in range(k,len(arr)):
        first_k[arr[i-k]]-=1
        if first_k[arr[i-k]]==0:
            del first_k[arr[i-k]]
        first_k[arr[i]]+=1
        res.append(len(first_k))
    return res

print(window([10, 20, 20, 10, 30, 40, 10], 4))
print(window([10, 10, 10, 10], 3))

print(naive([10, 20, 20, 10, 30, 40, 10], 4))
print(naive([10, 10, 10, 10], 3))

print(eff_window([10,20,20,10,30,40,10],4))
print(eff_window([10,10,10,10],3))