#######################O(n^2)############################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         prof = 0

#         length = len(prices)

#         for i in range(length):
#             for j in range(i + 1, length):
#                 if prices[j] > prices[i]:
#         	        if prices[j] -prices[i] > prof:
#         		        prof = prices[j] -prices[i]
#         return(prof)                




#######################O(n)############################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit

        