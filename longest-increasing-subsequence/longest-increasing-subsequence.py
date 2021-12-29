class Solution(object):
    def lengthOfLIS(self, nums):
        subs=[nums[0]]
        for num in nums[1:]:
            if num>subs[-1]:
                subs.append(num)
            else:
                i=0
                while num>subs[i]:
                    i+=1
                subs[i]=num
        return len(subs)
            
        """
        :type nums: List[int]
        :rtype: int
        """
        