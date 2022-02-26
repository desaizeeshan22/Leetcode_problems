class Solution(object):
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        hash_map={0:0}
        max_len=0
        sum_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            if sum_ in hash_map:
                max_len=max(i+1-hash_map[sum_],max_len)
            else:
                hash_map[sum_]=i+1
        return max_len
        """
        :type nums: List[int]
        :rtype: int
        """
        