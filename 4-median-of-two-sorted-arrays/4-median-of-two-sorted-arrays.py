class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        lo=0
        hi=n1
        while lo<=hi:
            cut1=lo+(hi-lo)//2
            cut2=(n1+n2+1)//2-cut1
            if cut1==0:
                l1=float("-inf")
            else:
                l1=nums1[cut1-1]
            if cut2==0:
                l2=float("-inf")
            else:
                l2=nums2[cut2-1]
            if cut1==n1:
                r1=float("inf")
            else:
                r1=nums1[cut1]
            if cut2==n2:
                r2=float("inf")
            else:
                r2=nums2[cut2]
            if l2<=r1 and l1<=r2:
                if(n1+n2)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                hi=cut1-1
            else:
                lo=cut1+1
        return 0.00
            
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        