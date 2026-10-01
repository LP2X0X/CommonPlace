from typing import List
# No duplicate triplets (like [1,2,3] and [2,1,3])
# KEY: Return ALL triplet, not just first one that sum = 0
# Return empty arrays if not found
# Return the number itself and not indexes

# Time: Three for loop O(n^3) - Space: Constant O(1)
def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    triplets = set()
    
    if n < 3:
        return []
    
    for i in range(n):
        for j in range(i + 1):
            for k in range(j + 2):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    
    return [list(triplet) for triplet in triplets]

# Observation: Consider the numbers a, b, c. If we hold the position of a, we then consider the remaining of the arrays, the problem become the pair sum problem. The only missing piece here that its not SORTED.
# Observation: To solve the duplication problem, we don't want to search the same a for combination. After we sorted, if we encountered the same number a, we skip it. We do the same for b (in case we are fixing the a number). For c, we don't have to deal with duplication because if a and b are unique, then c must also be unique.
# Optimization: Since for a sum of 3 numbers to be 0, at least one number must be negative (or all are 0), we can skip when a reach positive number.

# TIME:
# From the sort algo: O(nlog(n))
# From two pointer algo: O(n) for each n item => O(n^2) 
# Sum: O(n^2)

# SPACE:
# Without triplet O(n) from the sort algo
# With triplet result, n anchor need the worst case of n/2 pair which is roughly n in
# big O term. Therefore the space is O(n^2)

# MISTAKES:
# Use wrong arrays (unsorted one)
# Use if for skipping (shoule be while)

def triplet_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    
    results = [] 
    
    sortedNums = sorted(nums)
    
    for index, a in enumerate(sortedNums):
        # since we already sort the list and there could be a case where three 0s -> stop and no == 0
        if a > 0:
            break
        # next anchor is the same as previous -> skip
        if index > 0 and sortedNums[index - 1] == sortedNums[index]:
            continue
        
        left = index + 1
        right = len(sortedNums) - 1
        
        while left < right:
            sum = a + sortedNums[left] + sortedNums[right]
            if sum == 0:
                results.append([a, sortedNums[left], sortedNums[right]])
                left += 1
                # next b is the same as previous -> skip
                # You used to use if here, must use while
                while sortedNums[left] == sortedNums[left - 1]:
                    left += 1
            elif sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
        
    return results 