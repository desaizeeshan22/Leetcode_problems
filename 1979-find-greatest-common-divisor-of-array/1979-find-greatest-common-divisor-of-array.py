class Solution(object):
    def findGCD(self, nums):
        min_num=min(nums)
        max_num=max(nums)
        def gcd(a,b):
            while a!=b:
                if a>b:
                    a-=b
                else:
                    b-=a
            return a
        return gcd(min_num,max_num)
        """
        :type nums: List[int]
        :rtype: int
        """
        