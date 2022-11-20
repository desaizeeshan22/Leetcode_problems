class Solution(object):
    def runningSum(self, nums):
        res=[]
        res.append(nums[0])
        for i in range(1,len(nums)):
            res.append(res[i-1]+nums[i])
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """