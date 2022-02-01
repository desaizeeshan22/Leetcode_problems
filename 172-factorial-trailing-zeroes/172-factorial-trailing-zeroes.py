
class Solution(object):
    def trailingZeroes(self, n):
        res=0
        i=5
        while i<=n:
            res+=n//i
            i*=5
        return res
        """
        :type n: int
        :rtype: int
        """
        