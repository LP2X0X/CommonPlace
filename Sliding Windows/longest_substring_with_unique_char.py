# Brute force
def longest_substring_with_unique_char_brute_force (source: str) -> int:
    sourceLen = len(source)

    if sourceLen == 0:
        return 0
    elif sourceLen == 1:
        return 1
   
    longestLength = 1
    for start in range(sourceLen):
        # Mistake: Any range need to include the index of last item + 1
        for end in range(start + 1, sourceLen + 1):
            charCnt = {}
            length = 0
            subStr = source[start:end]
            for char in subStr:
                if char not in charCnt:
                    charCnt[char] = 1
                    length += 1
                else:
                    break
            longestLength = max(longestLength, length)

    return longestLength

# Observation
# Using sliding window to keep the number of unique char in a window
# When we met a nonduplicate char, we move the pointer right again and increase the count of the window  
# When we met a ducplicate char, we move the left pointer forward until the duplicate char is not in the window 
# The key insight is that you never need to move left backward. When right hits a duplicate, every window starting at left or earlier already contains that duplicate — so they can't beat the current best. You only need to check windows that start after the first copy of the duplicate character.

# TIME: O(n)
# SPACE: O(m) max 26 char hash map
def longest_substring_with_unique_char (source: str) -> int:
    longestLength = 0
    
    left = 0
    right = 0
    
    currentLength = 0
    charExistMap = {}
    while right < len(source):
        # in keyword check if the item EXIST or not
        if source[right] not in charExistMap:
            charExistMap[source[right]] = 1
            currentLength += 1
        else:
            # Think about edge case when the dup char is next to each other
            longestLength = max(longestLength, currentLength)
            while source[left] in charExistMap and source[left] != source[right]:
                # Therefore we must remove it instead of set it to 0
                del charExistMap[source[left]]
                left += 1
                currentLength -= 1
            # For when they reach the duplicate char, we move once more
            # Duplicate char will exist before right, that is guarantee
            left += 1
            # We also do not remove the count of the duplicate char here
            # We also do not also decrease the current length
        right += 1
    # Mistake: A window that reaches the end of the string need measured.
    return max(longestLength, currentLength)

# This solution answer the problem what if we use hash set instead?
def longest_substring_with_unique_char_improved (source: str) -> int:
    longestLength = 0
    
    left = 0
    right = 0
    
    # currentLength = 0 # Can be calculate by using left and right pointer
    charExistSet = set() # Use hash set in this case since 1 value can be represent by existance of the char
    while right < len(source):
        while source[right] in charExistSet:
            charExistSet.remove(source[left]) # Del until the exist duplicate char gone
            left += 1
        # Compare
        longestLength = max(longestLength, right - left + 1)
        charExistSet.add(source[right])
        right += 1
            
    # Mistake: A window that reaches the end of the string need measured.
    return longestLength

# What if we skip the left pointer traverse by teleport it to a position right after the first instance of the duplicate char? => Use hash map to store both the char and the index location 
# What happen to others char in the hash map since we do not remove them?
# Think... We must thinking in respect to the window
def longest_substring_with_unique_char_improved_more (source: str) -> int:
    maxLen = 0 # Better name!
    
    left = 0
    right = 0
    
    charExistMap = {}
    while right < len(source):
        # Why compare to left here? Like I said, we need to respect the window. And also, we do not remove the existing char that mapped in charExistMap => Only the char on the right side of the left pointer should be consider for duplication since its the begin of a new unique substring
        # Equal left in case the beginning of a unique substring is the duplicate char 
        if source[right] in charExistMap and charExistMap[source[right]] >= left:
            # Move 1 more time from the duplicate position
            left = charExistMap[source[right]] + 1
        
        maxLen = max(maxLen, right - left + 1)
        # Neat point when using map, we don't need to check if the key exist or not!
        charExistMap[source[right]] = right
        right += 1
        
    return maxLen