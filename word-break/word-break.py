class Solution(object):
    def wordBreak(self, s, wordDict):
        table=[False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i>=len(word)-1 and (table[i-len(word)] or i==len(word)-1 ):
                    if s[i-len(word)+1:i+1]==word:
                        table[i]=True
                        break
        return table[-1]
            
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        