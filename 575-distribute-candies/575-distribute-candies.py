class Solution(object):
    def distributeCandies(self, candyType):
        hash_set=dict()
        for elem in candyType:
            if elem not in hash_set:
                hash_set[elem]=0
            else:
                hash_set[elem]+=1
        n_unique=len(hash_set.keys())
        n_permitted=len(candyType)/2
        return  n_unique if n_permitted>=n_unique else n_permitted
        
        """
        :type candyType: List[int]
        :rtype: int
        """
        