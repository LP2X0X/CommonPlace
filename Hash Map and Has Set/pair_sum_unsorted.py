from typing import List

# Brute force will take O(n^2) since we will loop through every possible pair

# OBSERVATION:
# KEY: Return the indexes, not the values
# Order of the indexes does not matter 
# Input array are of integer type

# OBSERVATION:
# The problem can be view in a different way. We need to find a + b = target
# So when we have the number a, we need to find the target - a number (which is b)
# We also need a way to store both the index and the value so that we can return the index later => use hash map
# What should be the key, what should be the value?
# => KEY: The number should be the key, the index should be the value
# => We can look up the number with (target - a) in O(1) time

# We can traverse the array once, mapping the hash map then traverse it again, this time looking for the others number (b) if its in the map or not
# Then combine their indexes for the result
def pair_sum_unsorted_naive (nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    for i in range(len(nums)):
        num_map[nums[i]] = i
        
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []
# Did not evaluate for edge cases yet

print(pair_sum_unsorted_naive([0,0], 0))

# We need to find the complementary value (b) right?
# Why not store it as the key already (the complementary value b) with the value will be the index of the initial value (a)?
# This is a great way to utilize the O(1) search time
# TIME: O(n)
# SPACE: O(n) cause of hash map
def pair_sum_unsorted (nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    for i, num in enumerate(nums):
        # Mistake: We need to check it before we assign to the map since the new value could be the key we are looking for itself
        if i != 0 and num in num_map:
            return [i, num_map[num]]
        num_map[target - num] = i
    return []
    
print(pair_sum_unsorted([0,0], 0))