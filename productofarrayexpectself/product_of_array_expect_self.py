def productExceptSelf(nums):
    n = len(nums)
    answer = [0] * n

    # Calculate the product of prefixes
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
        print("this is prefix and answer:",prefix,answer)

    # Calculate the product of suffixes and multiply with prefixes
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
        print("this is suffix and answer:",suffix,answer)

    return answer


nums1 = [1, 2, 3, 4]
print(productExceptSelf(nums1))
# Output: [24, 12, 8, 6]

# nums2 = [-1, 1, 0, -3, 3]
# print(productExceptSelf(nums2))
# Output: [0, 0, 9, 0, 0]
