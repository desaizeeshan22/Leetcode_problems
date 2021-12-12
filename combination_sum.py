# Given an array of distinct integers candidates and a target integer target, return a list of
# all unique combinations of candidates where the chosen numbers sum to target.You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.Two combinations are unique if the
# frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.


def combination_sum(candidates,target):
    results=[]
    def backtrack(remainder,comb,start):
        if remainder==0:
            results.append(list(comb))
            return
        if remainder<1:
            return
        for index in range(start,len(candidates)):
            comb.append(candidates[index])
            backtrack(remainder-candidates[index],comb,index)
            comb.pop()
    backtrack(target,[],0)
    return results

print(combination_sum([2,3,6,7],7))