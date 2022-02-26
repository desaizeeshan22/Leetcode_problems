from collections import Counter
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        curr=1
        res=1
        hash_map=Counter(nums)
        for elem in hash_map:
            if elem-1 not in hash_map:
                curr=1
                while elem+curr in hash_map:
                    curr+=1
                res=max(res,curr)
        return res
                
        """
        :type nums: List[int]
        :rtype: int
        """
        