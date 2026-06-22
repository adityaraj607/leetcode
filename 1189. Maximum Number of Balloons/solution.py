class Solution(object):
    def maxNumberOfBalloons(self, text):
        map={"b":0,"a":0,"l":0,"o":0,"n":0}
        instances=0
        for i in text.lower():
            if i in "balloon":
                map[i]+=1
        while (map["b"]>=1 and map["a"]>=1 and map["l"]>=2 and map["o"]>=2 and map["n"]>=1):
            instances+=1
            map["b"]-=1
            map["a"]-=1
            map["l"]-=2 
            map["o"]-=2 
            map["n"]-=1
        return instances
