

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n
        
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
        
        return result
    
# -------------------------------------------------------------------
    
# def problem(nums):
#     length = len(nums)
#     pre_fix = [1] * length
#     post_fix = [1] * length
#     result = length * [1]
#     key = 1
#     for i in range(length):
#         pre_fix[i] = pre_fix[i-1] * nums[i]
    
#     pre_fix.insert(0,1)
#     pre_fix.pop()
    
#     for i in range(length-1,-1,-1):
#             post_fix[i] = key * nums[i]
#             key = post_fix[i]
#     post_fix.insert(length,1)
#     post_fix.pop(0)

#     print(pre_fix,post_fix)
    
#     for i in range(length):
#         result[i] = pre_fix[i] * post_fix[i]
#     return result

# print(problem(nums))

