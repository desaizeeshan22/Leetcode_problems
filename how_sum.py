## Write a function cansum to return an array of  combinations using numbers from the array
# generating a target sum (numbers maybe repeated) any one combination is the correct answer
def how_sum(target_sum,numbers,memo={}):
    """numbers (array): array of numbers
    target_sum:int the target sum to be achieved using the above array of numbers"""
    if target_sum in memo:
        return memo[target_sum]
    if target_sum<0:
        return None
    if target_sum==0:
        return []
    for elem in numbers:
        remainder=target_sum-elem
        res=how_sum(remainder,numbers,memo)
        memo[remainder]=res
        if res is not None:
            res.append(elem)
            return res
    return None

##m: target sum
##n : size of the array
## Time: O(n^m*m) worst-case without memoization aka brute force approach
##Space : O(m)

##memoized
#Time:O(n*m*m)
#Space:O(m^2)
print(how_sum(7,[5,3,4,7]))
print(how_sum(300,[7,14]))