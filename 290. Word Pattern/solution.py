class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map={}
        map2={}
        if len(s.split())!=len(pattern):
                return False
        for i in range(len(pattern)):
            if pattern[i] in map and map[pattern[i]]!=s.split()[i]:
                return False
            elif s.split()[i] in map2 and map2[s.split()[i]]!=pattern[i]:
                return False
            else:
                map[pattern[i]]=s.split()[i]
                map2[s.split()[i]]=pattern[i]
        return True
