class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force... O(N^2)
        # max_profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i] 
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(prices[j] - buy, max_profit)
        # return max_profit

        # 2 ptr
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices): 
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r = r + 1
        return max_profit