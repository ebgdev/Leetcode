##################### 1 #########################
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return[i, j]
          
target = 6
nums = [3, 2, 4]
deneme = Solution()
print(deneme.twoSum(nums, target))

##################### 2 #########################

class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index, val in enumerate(nums):
            rem = target - val
            if rem in d:return [d[rem], index]
            d[val] = index


target = 6
nums = [3, 2, 4]

deneme = Solution()
print(deneme.twoSum(nums, target))











