class Solution(object):
    def shipWithinDays(self, weights, days):
        def is_possible(weights,days,threshold):
            w_packages=0
            D=1
            for i in range(len(weights)):
                if weights[i]>threshold:
                    return False
                if weights[i]+w_packages>threshold:
                    w_packages=weights[i]
                    D+=1
                else:
                    w_packages+=weights[i]
            return False if D>days else True
        res=-1
        l_max=max(weights)
        h_max=sum(weights)
        while l_max<=h_max:
            mid=(l_max+h_max)//2
            if is_possible(weights,days,mid):
                res=mid
                h_max=mid-1
            else:
                l_max=mid+1
        return res
            
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """