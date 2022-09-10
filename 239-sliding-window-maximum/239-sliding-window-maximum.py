class Solution(object):
    def maxSlidingWindow(self, nums, k):
        def clean_deque(i,deq):
            if deq and deq[0]==i-k:
                deq.popleft()
            while deq and nums[i]>nums[deq[-1]]:
                deq.pop()
        deq=deque()
        max_index=0
        for i in range(k):
            clean_deque(i,deq)
            deq.append(i)
            if nums[i]>nums[max_index]:
                max_index=i
        output=[nums[max_index]]
        for i in range(k,len(nums)):
            clean_deque(i,deq)
            deq.append(i)
            output.append(nums[deq[0]])
        return output
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        