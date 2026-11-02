from typing import List 
#Find the longest chain of consecutive numbers in an array. Two numbers are consecutive if they have a difference of 1.
#Example:
#Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
#Output: 4
#Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
# CONSTRAINT: Could there be duplicate?

# KEY: They do not have to be in index orders
# KEY: Return the length of the chain

# TIME: O(nLog(n))
# SPACE: O(1)
def brute_force_way (nums: List[int]) -> int:
    if len(nums) == 0: 
        return 0
    if len(nums) == 1: 
        return 1
    
    sortedNums = sorted(nums) # O(nLog(n)) best
    longestLength = 0
    length = 1
    for i in range(len(nums) - 1):
        if sortedNums[i + 1] == sortedNums[i] + 1:
            length += 1
        elif sortedNums[i + 1] == sortedNums[i]:
            continue
        else:
            length = 1
        longestLength = max(longestLength, length)
    return longestLength 

print(brute_force_way([1, 6, 2, 5, 8, 7, 10, 3]))

# OBSERVATION: In our brain, pick any number, start with that then we search for the next one in the list if it exist or not. A quick scan give us the result of the test case is 4. Is there a way to quickly search if a number exist or not? Hash set   

# OBSERVATION: But then, should we do it for all numbers? Intuitively, we should find a way to search only from the smallest value in the chain, right?
# We can do that by checking if there is any value - 1 number exist.

# TIME: Convert to set O(n), traverse the list O(n), the inner while loop will only took O(n). Why is it not a nested loop which mean O(n^2)? Because each number can only exist in one chain, if it exist in another means there is a lap between them so technically they are still one chain. That means with the inner while loop, we check each numbers only once. Therefore, the sum of the inner while loop took O(n) time. => O(3n) = O(n) 
# SPACE: O(n) for the set
def longest_chain_of_consecutive_numbers (nums: List[int]) -> int:
    longestLength = 0
    numSet = set(nums)
    
    for num in nums:
        if num - 1 not in numSet:
            length = 1
            val = num + 1
            while val in numSet:
                length += 1
                val += 1
            longestLength = max(longestLength, length)
            
    return longestLength