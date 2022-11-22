class Solution(object):
    def isSubsequence(self, s, t):
        if(len(s)>len(t)):
            return False
        if(len(s)==0):
            return True
        i=j=0
        while(i<len(s) and j<len(t)):
            if(s[i]==t[j]):
                i+=1
            j+=1
        if(i==len(s)):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        