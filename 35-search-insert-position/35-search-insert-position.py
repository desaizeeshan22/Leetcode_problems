class Solution(object):
    def searchInsert(self, nums, target):
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if target>nums[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return lo
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        