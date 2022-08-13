from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output=[]
        d=deque()
        max_index=0
        def clean_deque(deq,i,k,nums):
            if(deq and deq[0]==i-k):
                deq.popleft()
            while(deq and nums[i]>nums[deq[-1]]):
                deq.pop()    
        for i in range(0,k):
            clean_deque(d,i,k,nums)
            d.append(i)
            if(nums[i]>nums[max_index]):
                max_index=i
        output.append(nums[max_index])
        for i in range(k,len(nums)):
            clean_deque(d,i,k,nums)
            d.append(i)
            output.append(nums[d[0]])    
        return output

    
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        