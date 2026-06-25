class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map1={}
        map2={}
        for i in s:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        for i in t:
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1
        for i in map2:
            if i not in map1:
                return i
            elif map1[i]!=map2[i]:
                return i
