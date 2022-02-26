class Solution(object):
    def subarraySum(self, nums, k):
        hash_map={0:1}
        sum_=0
        count=0
        for elem in nums:
            sum_+=elem
            
            if sum_-k in hash_map:
                count+=hash_map[sum_-k]
            hash_map[sum_]=hash_map.get(sum_,0)+1
        return count
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        