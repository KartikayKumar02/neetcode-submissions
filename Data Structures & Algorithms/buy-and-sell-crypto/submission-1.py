class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        right = 1  # assume sell day
        left = 0 #buy day

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit,profit)
            else:
                left = right
            right += 1
        return maxprofit
                