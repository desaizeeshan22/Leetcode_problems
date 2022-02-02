class Solution(object):
    def minSteps(self, n):
        def min_steps(n,memo={}):
            if n in memo:
                return memo[n]
            if n==0 or n==1:
                return 0
            for i in range(n-1,0,-1):
                if n%i==0:
                    memo[n]=n//i+min_steps(i,memo)
                    return memo[n]
        return min_steps(n)
        """
        :type n: int
        :rtype: int
        """
        