class Solution(object):
    def intersection(self, nums1, nums2):
        s1=set(nums1)
        res=[]
        for elem in nums2:
            if elem in s1 and elem not in res:
                res.append(elem)
        return res
            
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        