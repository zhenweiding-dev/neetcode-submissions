class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i prices:[int]
        o int single buy and sell
        c len in [1,100], int in[0,100]
        e 
        use two pointers to track lower price to buy and higher
        price to sell
        from begining, if left is higher, update left
        if right is higher, update profit and move right
        """
        buy, sell = 0, 1
        profitMax = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profitMax = max(profitMax, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profitMax

        