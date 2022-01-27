class Solution(object):
    def minSubArrayLen(self, target, nums):
        size=float("inf")
        left=0
        sum_=0
        for i,v in enumerate(nums):
            sum_+=v
            while(sum_>=target):
                size=min(size,i-left+1)
                sum_-=nums[left]
                left+=1
                
        return size if size!=float("inf") else 0
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        