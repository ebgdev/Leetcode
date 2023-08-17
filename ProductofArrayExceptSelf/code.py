class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
	        arr = nums[:i]+nums[i+1:]
	        new_arr.append(reduce(lambda x, y: x*y, arr))
        return new_arr