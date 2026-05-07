class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])

            else:
                # Update the left to the lowest point
                left = right

            right +=1

        return maxProfit

            