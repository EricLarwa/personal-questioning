## create a two pointer system
# a max profit integer to keep track of the profit
# max function of maxProfit to see if, as you iterate through the list, 
# what numbers return most profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        return maxP
        