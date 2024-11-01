# 0ms runtime

from typing import List
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = Counter(nums)
        
        for i, item in enumerate(nums):
            diff = target - item
            # Check if diff exists and handles cases when `diff` equals `item`
            if diff in my_dict and (diff != item or my_dict[diff] > 1):
                # Find indices for both items
                j = nums.index(diff, i + 1) if diff == item else nums.index(diff)
                return [i, j]
        
        return []