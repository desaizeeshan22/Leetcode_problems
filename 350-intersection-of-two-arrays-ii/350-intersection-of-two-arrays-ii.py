from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        c1=Counter(nums1)
        c2=Counter(nums2)
        res=[]
        for elem in c1.keys():
            if elem in c2:
                i=min(c1[elem],c2[elem])
                while i>0:
                    res.append(elem)
                    i-=1
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        