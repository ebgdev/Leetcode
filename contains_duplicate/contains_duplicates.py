####################### 1 ############################
# def has_duplicates(nums):
#     dic = {}
#     nums_count = 0
#     for i in nums:
#         nums_count += 1
#         dic[i] = i
    
#     if len(dic) < nums_count:
#         return True
#     else:
#         return False


# nums = [1, 2, 5, 6, 7, 2, 5]
# result = has_duplicates(nums)
# print(result)


####################### 2 ############################
# this version is better
def has_duplicates(nums):
    my_set = set(nums)
    if len(my_set) < len(nums):
    	return True
    else: 
    	return False

nums = [1, 2, 5, 6, 7, 2, 5]
result = has_duplicates(nums)
print(result)
