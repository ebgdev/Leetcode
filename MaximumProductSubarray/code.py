#galah bir gismat mosbatla saxliya axir lahziyajan 
#bir gismat da manfilari chon manfilar eliabilar mosbata chona bir lahza
# va chon manfilarda da adadan manfitare axdarerux ona gora galah min 
#estefade eliyax va alamate chox mohem dayir o lahza


from typing import List

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         product = 1
#         max_product = float("-inf")
#         min_product = 1

#         for num in nums:
#             if num == 0:
#                 product = 1
#                 max_product = max(max_product, 0)
#                 min_product = 1
#             else:
#                 temp = product
#                 product = max(num, num * product, num * min_product)
#                 min_product = min(num, num * temp, num * min_product)

#                 max_product = max(max_product, product)

#         return max_product

# nums9 = [2,-5,-2,-4,3,-5,1,1,1,-12]
# erfan = Solution()
# print(erfan.maxProduct(nums9))



# -----------------5-------------------# -----------------5-------------------


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin,curMax = 1,1

        for n in nums:
            if n == 0:
                curMin,curMax = 1,1
                continue

            print(n)    
            temp = curMax * n
            print(temp)
            curMax = max(n*curMax,n*curMin,n)
            print(curMax)
            curMin = min(temp,n*curMin,n)
            print(curMin)
            res = max(res,curMax)
            print(res)

        return res


erfan = Solution()
erfan.maxProduct([-2,0])


