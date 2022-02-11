from collections import Counter
class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.nums1=nums1
        self.nums2=nums2
        self.hash_map=Counter(nums2)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        

    def add(self, index, val):
        self.hash_map[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.hash_map[self.nums2[index]]+=1
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def count(self, tot):
        count=0
        for elem in self.nums1:
            count+=self.hash_map[tot-elem]
        return count
        """
        :type tot: int
        :rtype: int
        """
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)