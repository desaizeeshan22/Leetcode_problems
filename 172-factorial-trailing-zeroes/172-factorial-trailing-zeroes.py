import math
class Solution(object):
    def trailingZeroes(self, n):
        res=0
        i=5
        while i<=n:
            res+=math.floor(n/i)
            i*=5
        return int(res)
        """
        :type n: int
        :rtype: int
        """
        