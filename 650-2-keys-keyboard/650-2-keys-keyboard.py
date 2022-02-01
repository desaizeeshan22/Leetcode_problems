class Solution(object):
    def minSteps(self, n):
        def min_steps(n):
            if n==0 or n==1:
                return 0
            for i in range(n-1,0,-1):
                if n%i==0:
                    return n//i+min_steps(i)
        return min_steps(n)
        """
        :type n: int
        :rtype: int
        """
        