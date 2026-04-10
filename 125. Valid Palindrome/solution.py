class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news=""
        for i in s.lower():
            if i.isalnum():
                news+=i
        return news==news[::-1]