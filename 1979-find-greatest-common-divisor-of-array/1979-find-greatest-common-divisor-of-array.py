class Solution(object):
    def findGCD(self, nums):
        min_num=min(nums)
        max_num=max(nums)
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        return gcd(min_num,max_num)
        """
        :type nums: List[int]
        :rtype: int
        """
        