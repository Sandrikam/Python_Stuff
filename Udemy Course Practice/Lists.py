def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num += 1

 # (Fill in the missing line here)
            return max_num

find_max(5)