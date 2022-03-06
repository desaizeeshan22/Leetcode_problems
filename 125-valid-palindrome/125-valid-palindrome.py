class Solution(object):
    def isPalindrome(self, s):
        def clean_str(string):
            res=""
            string=string.lower()
            for c in string:
                if c.isalnum() and c!=" ":
                    res+=c
            return res
        s=clean_str(s)
        def is_palindrome(string):
            n=len(string)
            for i in range(n):
                if string[i]!=string[n-1-i]:
                    return False
            return True
        return is_palindrome(s)
                
        """
        :type s: str
        :rtype: bool
        """
        