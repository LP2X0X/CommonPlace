from typing import List

# OBSERVATION
# Initial: Traverse the list, if the pointer point to a non-zero, add it to another list, keep a number of zero encountered along the way then append to the new list when the pointer reach the end.
# KEY: Return the new array

# TIME: O(n) aktually O(2n) but you know... 
# Space: O(n) for the creation of a new array 
def initial_shift_zeros_to_the_end(nums: List[int]) -> List[int]:
    zeroEndedNums = []
    numOfZeros = 0
    pointer = 0
    for pointer in range(len(nums)):
        if nums[pointer] != 0:
            zeroEndedNums.append(nums[pointer])
        else:
            numOfZeros += 1
    for zero in range(numOfZeros):
        zeroEndedNums.append(0)
    
    return zeroEndedNums 
    
# TEST CASE:
# print(initial_shift_zeros_to_the_end([]))
# print(initial_shift_zeros_to_the_end([0]))
# print(initial_shift_zeros_to_the_end([1]))
# print(initial_shift_zeros_to_the_end([0, 0, 0]))
# print(initial_shift_zeros_to_the_end([1, 2, 3]))
# print(initial_shift_zeros_to_the_end([1, 1, 1, 0, 0]))
# print(initial_shift_zeros_to_the_end([0, 0, 0, 1, 1]))

# OBSERVATION
# Initial: ~~Use one pointer as an anchor for the position of the zero we will move while one pointer actively traverse the list to find it~~ This make reorder them a night mare...
# KEY 1: Modify the array IN PLACE
# Instead of thinking how to move the zero to end of the list, lets think about how to move the non-zero to the left... One pointer to mark the position of the next available position for the non-zero to move in. One pointer to find it.
# KEY 2: The trail left by the traverse pointer already contains only zero numbers

# what's next for anchorPointer (except the first index item) always be zero since traversePointer always looking for them and replace them for anchorPointer to move next

# TIME: O(n)
# SPACE: O(1)
def shift_zeros_to_the_end(nums: List[int]) -> List[int]:
    anchorPointer = 0
    
    # Use for loop as a way of traverse itself
    for traversePointer in range(len(nums)):
        # Edge case where the first item is non-zero, it will just replace itself
        if nums[traversePointer] != 0:
            nums[anchorPointer], nums[traversePointer] = nums[traversePointer], nums[anchorPointer]
            # Anchor pointer when point at the first position could be pointing to a non-zero, so writing this could f it all up
                # nums[anchorPointer] = nums[traversePointer]
                # nums[traversePointer] = 0
            anchorPointer += 1 # Plus one because of KEY 2
        
    return nums

# TEST CASES:
print(shift_zeros_to_the_end([]))
print(shift_zeros_to_the_end([0]))
print(shift_zeros_to_the_end([1]))
print(shift_zeros_to_the_end([0, 0, 0]))
print(shift_zeros_to_the_end([1, 2, 3]))
print(shift_zeros_to_the_end([1, 1, 1, 0, 0]))
print(shift_zeros_to_the_end([0, 0, 0, 1, 1]))