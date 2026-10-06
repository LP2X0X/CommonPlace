from typing import List

# Brute force 
# Loop through all combinations of vertical lines
# KEY: return the largest volume, not what vertical line values or their index make up that value
# TIME: O(n^2)
# SPACE: O(1)
def brute_force_largest_container (heights: List[int]) -> int:
    maxVol = 0; 
    # Edge case where heights contain no item or one item
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            vol = (j - i) * min(heights[i], heights[j]) 
            if vol > maxVol:
                maxVol = vol
    return maxVol

# OBSERVATION
# The set up for this problem directly point to two pointer technique
# The index interval length decrease when we move the pointers inward
# Only the smaller height value will be used to calculate the current volume
# Stop when left >= right
# When both heights are equal, moving either one alone can only make things worse or stay the same — because the width shrinks by 1 but the height can't increase (it's capped by the shorter side, which is the same). So move both pointers inward since staying with either one is pointless

# TIME: O(n), well aktually its O(n/2)
# SPACE: O(1) cause constant number of vars
def largest_container (heights: List[int]) -> int:
    maxVol = 0
    
    width = len(heights)
    
    leftColIdx = 0
    rightColIdx = width - 1
    
    while leftColIdx < rightColIdx:
        # Volume = Height * Width
        # Height: Smaller height 
        # Width: Interval between two pointers
        vol = min(heights[leftColIdx], heights[rightColIdx]) * (rightColIdx - leftColIdx)
        if vol > maxVol:
            maxVol = vol
            
        if heights[leftColIdx] > heights[rightColIdx]:
            rightColIdx -= 1
        elif heights[leftColIdx] < heights[rightColIdx]:
            leftColIdx += 1
        else:
            leftColIdx += 1
            rightColIdx -= 1
    
    return maxVol

print(largest_container([]))
print(largest_container([1]))
print(largest_container([0, 1, 0]))
print(largest_container([3, 3, 3, 3]))
print(largest_container([1, 2, 3]))
print(largest_container([3, 2, 1]))