class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        res=[]
        while i<j:
            if numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]==target:
                res.append(i+1)
                res.append(j+1)
                i+=1
                j-=1
            else:
                i+=1
        return res
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        