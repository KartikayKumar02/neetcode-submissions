
# prices = [10,1,5,6,7,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        maxprofit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxprofit = max(maxprofit,prices[right] - prices[left])   # 4,5,6 
            else:
                left = right 
            right += 1
        return maxprofit



        