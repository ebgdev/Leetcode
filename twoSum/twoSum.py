from typing import List


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# -----------------1



# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#       my_hash = {}
#       length = len(nums)
#       for i in range(length):
#           my_hash[nums[i]] = i

#           for i in range(length):
#               complement = target - nums[i]
#               if complement in my_hash and my_hash[complement]!= i:
#                   return [i,my_hash[complement]]




# nums = [2,7,11,15]
# target = 9

# my_obj = Solution()
# print(my_obj.twoSum(nums,target))

# -----------------2



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        length = len(nums)

        for i,num in enumerate(nums):
            diff = target - num
            if diff in my_hash:
                return [my_hash[diff],i]

            my_hash[num] = i 
            #this is the best way to add key,values because at first hand we don't need to check anythinh at first


nums = [2,7,11,15]
target = 9

my_obj = Solution()
print(my_obj.twoSum(nums,target))



##################### 3 #########################
class Solution:
    #O(n^2)
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





