
class Solution(object):
    def trailingZeroes(self, n):
        res=0
        while n>0:
            n//=5
            res+=n
        return res
        """
        :type n: int
        :rtype: int
        """
        