
def how_sum(target_sum,numbers,result=[]):
    """numbers (array): array of numbers
    target_sum:int the target sum to be achieved using the above array of numbers"""
    # key=(target_sum,str(numbers))
    # if key in memo:
    #     return memo[key]
    if target_sum<0:
        return None
    if target_sum==0:
        return []
    for elem in numbers:
        remainder=target_sum-elem
        res=how_sum(remainder,numbers,result)
        if res is not None:
            res.append(elem)
            return res
    return None




print(how_sum(7,[5,3,4,7]))