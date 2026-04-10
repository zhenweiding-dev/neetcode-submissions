class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i prices:[int]
        o int single buy and sell
        c len in [1,100], int in[0,100]
        e 
        use minBuy to track lowest price so far
        use maxProfit to track each price - minBuy and update to highest
        """
        minBuy = prices[0]
        maxProfit = 0
        for p in prices:
            minBuy = min(minBuy, p)
            maxProfit = max(maxProfit, p - minBuy)
        return maxProfit
        

        