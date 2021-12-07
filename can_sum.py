## Write a function cansum to return a boolean value indicating whether or not it is possible to
# generate a target sum using numbers from the array

def cansum(target_sum,numbers,memo={}):
    """numbers (array): array of numbers
    target_sum:int the target sum to be achieved using the above array of numbers"""
    key=(target_sum,str(numbers))
    if key in memo:
        return memo[key]
    if (target_sum==0):
        return True
    if target_sum<0:
        return False
    for elem in numbers:
        remainder=target_sum-elem
        if cansum(remainder,numbers,memo):
            memo[key]=True
            return True
    memo[key] = False
    return False

print(cansum(8,[2,3,5]))
print(cansum(7,[2,4]))
print(cansum(300,[7,14]))
