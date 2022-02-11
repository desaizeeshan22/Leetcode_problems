
class Solution(object):
    def singleNonDuplicate(self, nums):
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            even_halves=(hi-mid)%2==0
            if nums[mid-1]==nums[mid]:
                if even_halves:
                    hi=mid-2
                else:
                    lo=mid+1
            elif nums[mid+1]==nums[mid]:
                if even_halves:
                    lo=mid+2
                else:
                    hi=mid-1
            else:
                return nums[mid]
        return nums[lo]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        