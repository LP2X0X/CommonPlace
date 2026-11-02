from typing import List

# They request a pair of sum, so one item is not enough
# What happen if there are no items
# KEY: Notice that the list is sorted => inward two pointer 
# They do not require a list of pair
# Time: Maximum number of traverse O(n) - Space: Constant var created => O(1)
# Those left-of-left elements were too small to reach the target even with a larger right value. They definitely can't reach it with the current smaller right value.
def pair_sum_sorted_two_pointer_inward(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1 
        
    return []
        


# TEST CASES
print(pair_sum_sorted_two_pointer_inward([], 0))
print(pair_sum_sorted_two_pointer_inward([1], 1))
print(pair_sum_sorted_two_pointer_inward([2,3], 5))
print(pair_sum_sorted_two_pointer_inward([2,4], 4))

            
        
        
        
    