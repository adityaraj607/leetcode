class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        max = 0
        for i in prices:
            if i < lowest:
                lowest = i
            if i - lowest > max:
                max = i - lowest
        return max
