class Solution(object):
    def maxSubArrayLen(self, nums, k):
        sum_=0
        max_len=0
        hash_map={}
        for i in range(len(nums)):
            sum_+=nums[i]
            if sum_==k:
                max_len=i+1
            if sum_-k in hash_map:
                max_len=max(i+1-hash_map[sum_-k],max_len)
            elif sum_ not in hash_map:
                hash_map[sum_]=i+1
        return max_len
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        