class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mp = {'2': "abc", '3': "def", '4': "ghi",'5': "jkl", '6': "mno",'7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = [""]
        for i in digits:
            temp = []
            for r in res:
                for c in mp[i]:
                    temp.append(r + c)
            res = temp
        return res      