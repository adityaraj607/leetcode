class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        n=0
        for i in sorted(costs):
            if i<=coins:
                coins-=i
                n+=1
        return n

        
