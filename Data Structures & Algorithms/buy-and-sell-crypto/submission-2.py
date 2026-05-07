class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Need two pointers
        # Need a profit storage
        # Get through the prices->check the profit, if not get any profit->update pointer
        
        #=================#====================#
        p1, p2 = 0, 1
        maxP = 0
        # Getting through all the prices until the end
        while p2 < len(prices):
            # If these is profit -> get the max profit
            # else -> update pointer 1 to the position of pointer 2
            if prices[p1] < prices[p2]:
                # Get the max profit so far
                maxP = max(maxP, prices[p2]-prices[p1])
            else:
                p1 = p2
            p2 +=1

        return maxP

            

            