def reverse(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def next_biggest_permutation(arr):
    n=len(arr)
    for j in range(n - 1, 0, -1):
        if arr[j - 1] < arr[j]:
            break
    if j == 1 and arr[j] <= arr[j - 1]:
        return reverse(arr)
    hash_map = {}
    diff = float("inf")
    for I in range(j, n):
        diff = min(diff, abs(arr[I] - arr[j - 1]))
        if diff not in hash_map:
            hash_map[diff] = I
    arr[hash_map[diff]], arr[j - 1]=arr[j - 1],arr[hash_map[diff]]
    arr[j:]=reverse(arr[j:])
    return arr

print(next_biggest_permutation([1, 3, 8, 4,7,6,5,1]))
print(next_biggest_permutation([1, 2,3]))
print(next_biggest_permutation([3,2,1]))