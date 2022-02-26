
class Solution(object):
    def intersect(self, nums1, nums2):
        def inter(nums1,nums2):
            if len(nums1)>len(nums2):
                return inter(nums2,nums1)
            d1=dict()
            for elem in nums1:
                d1[elem]=d1.get(elem,0)+1
            res=[]
            for elem in nums2:
                if d1.get(elem,0)>0:
                    res.append(elem)
                    d1[elem]-=1
            return res
        return inter(nums1,nums2)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        