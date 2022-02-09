class Solution(object):
    def findTheWinner(self, n, k):
        friends_list=[i for i in range(1,n+1)]
        i=0
        step_eliminate=k-1
        while len(friends_list)>1:
            i=(i+step_eliminate)%len(friends_list)
            del friends_list[i]
        return friends_list[0]
        
        """
        :type n: int
        :type k: int
        :rtype: int
        """