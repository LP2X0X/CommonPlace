# Given two strings, s and t, both consisting of lowercase English letters, return the number of substrings in s that are anagrams of t.
# 
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# 
# Example:
# 
# Input: s = "caabab", t = "aba"
# Output: 2
# 
# Explanation: There is an anagram of t starting at index 1 ("caabab") and another starting at index 2 ("caabab")
# KEY: Overlap substring is ok


# Observation
# Based on the definition of anagram, we can see that:
#    - The length of the substring is fixed (must match t)
# => We can use fixed sliding window technique
#    - The order of the letters in the anagram is trivial
# => We can use a hash map to store all the letters in the alphabet (lower case only? should have ask this before doing anything). The keys are the letters and the values is the number of each in the substring.
# KEY: Lower case letter only
# We create an array for counting the numbers of times a char appear in t.

# We know that a in anscii is 97 => Convert the letters to anscii number - 97 to get the index => O(1) access

# What to return? int (the number of substring satisfy)

# TIME: O(n)
# SPACE: O(1)
def substring_anagrams(source: str, target: str) -> int:
    # Edge case
    if len(target) > len(source):
        return 0
    
    anagramCnt = 0
    leftPtr = 0
    rightPtr = 0
    
    traverseWindow = [0] * 26 # 26 letters
    expectedWindow = [0] * 26 
    for i in range(len(target)):
        expectedWindow[ord(target[i]) - 97] += 1
        traverseWindow[ord(source[i]) - 97] += 1
        rightPtr += 1
    
    while rightPtr <= len(source):
        # Compare the two list
        isAdd = True
        for i in range(len(expectedWindow)):
            if expectedWindow[i] != traverseWindow[i]:
                isAdd = False
                break
        if isAdd:
            anagramCnt += 1

        # Traverse
        # Mistake: Order of statements are important here...
        # Mistake: Use ptr directly without convert first to ord...
        if rightPtr != len(source):
            traverseWindow[ord(source[leftPtr]) - 97] -= 1
            leftPtr += 1
            traverseWindow[ord(source[rightPtr]) - 97] += 1
            rightPtr += 1
    return anagramCnt

def substring_anagram_hash_map(source: str, target: str) -> int:
    anagramCnt = 0
    sourceLen = len(source)
    targetLen = len(target)
    if targetLen > sourceLen:
        return anagramCnt
    
    leftPtr = 0
    rightPtr = 0
    targetHashMap = {}
    sourceHashMap = {} 
    for i in range(targetLen):
        if ord(target[i]) - 97 not in targetHashMap:
            targetHashMap[ord(target[i]) - 97] = 1 
        else: 
            targetHashMap[ord(target[i]) - 97] += 1 
            
        if ord(source[i]) - 97 not in sourceHashMap:
            sourceHashMap[ord(source[i]) - 97] = 1 
        else: 
            sourceHashMap[ord(source[i]) - 97] += 1 
        # Keep the window size equal to target string size
        if rightPtr != targetLen - 1:
            rightPtr += 1
    
    while rightPtr < sourceLen: 
        # Compare
        addToAnagramCnt = True
        for key in targetHashMap:
            # Mistake: Use get here in case that key does not exist in sourceHashMap
            if targetHashMap[key] != sourceHashMap.get(key, 0):
                addToAnagramCnt = False
                break
        if addToAnagramCnt:
            anagramCnt += 1
            
        # Stop traverse when right ptr already at the last char and it has been compare
        if rightPtr == sourceLen - 1:   
            break

        # Traverse
        # Remove count of that char before move pointer
        sourceHashMap[ord(source[leftPtr]) - 97] -= 1
        leftPtr += 1
        # Move pointer than add count
        rightPtr += 1
        if ord(source[rightPtr]) - 97 not in sourceHashMap:
            sourceHashMap[ord(source[rightPtr]) - 97] = 1 
        else: 
            sourceHashMap[ord(source[rightPtr]) - 97] += 1 
    
    return anagramCnt
                
        
        
        