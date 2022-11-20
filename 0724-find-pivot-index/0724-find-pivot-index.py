class Solution(object):
    def pivotIndex(self, nums):
        if(len(nums)==1 or len(nums)==0):
            return 0
        precomputed_sums={}
        pre_sum=0
        for i in range(len(nums)):
            pre_sum+=nums[i]
            precomputed_sums[i]=pre_sum
    
        for i in range(len(nums)):
            left_sum=precomputed_sums[i]-nums[i]
            right_sum=precomputed_sums[len(nums)-1]-precomputed_sums[i]
            if(right_sum==left_sum):
                return i
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        