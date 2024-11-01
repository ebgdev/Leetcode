from typing import List
# 53.
# Attention there is no need to save the actual subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            max_sub = max(max_sub, curSum)
        return max_sub

object = Solution()
