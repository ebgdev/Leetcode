# This is my solution 
#in order to solve this problem we should 
#find where the portion are we looking at [3,4,5,6,7,8,1,2]
#the trick is when mid=7 is > left ,it means that is also bigger 
# the every value in right portion so the portion we should look in order to 
# find min value is also in the right portion [7,8,1,2]



class Solution:
    def findMin(self, array: List[int]) -> int:
        length = len(array)
        #handling the empty list and list with just one element
        match length:
            case 1:
                return array[0]
            case 0:
                return 'This List is empty'

        #handling if list is sorted already
        mid_value = array[len(array)//2]
        if mid_value and array[length-1] > array[0]:
            return array[0]
             
        #handling the Rotated List

        min_value = float('inf')
        right = length-1
        left = 0
        mid = (right+left)//2
        while left <= right:

            if array[mid] > array[left]:

                min_value = min(min_value,array[mid],array[left],array[right])
                left = mid +1
                mid = (left+right)//2

            else:

                min_value = min(min_value,array[mid],array[left],array[right])
                right = mid -1
                mid = (left+right)//2

        return min_value



# And this is others solution

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         # if nums[left] <= target < nums[mid]
#         # else 

#         start = 0
#         end = len(nums) - 1
#         prev = -1

#         while start < end:
#             mid = (start + end) // 2
#             if nums[mid] > nums[prev]:
#                 start = mid + 1
#                 prev = mid
#             else:
#                 end = mid
#                 prev = mid

#         return nums[start]