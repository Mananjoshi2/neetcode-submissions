class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # basic: nest for loop 
        # optimal: sliding window 

        result = 0  #running total result
        left = 0 # buy day

        for right in range(len(prices)):
            if prices[right] < prices[left]: # do i have a cheaper buy day?
                left = right  # if i do make today the buy day
            profit = prices[right] - prices[left]  # whats the profit
            result = max(profit, result)    # always update result 

        return result




        