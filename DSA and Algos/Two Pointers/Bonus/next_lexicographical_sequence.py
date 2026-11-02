from typing import List

# UNDERSTANDING THE PROBLEM
# What is the next lexicographical sequence of a string is?
# Imagine each character holds a value:
# a = 1, b = 2, c = 3
# Given the string abc: => represent value: 123
# The next lexicographical permutation of this string is the next larger value can be represent by it when we change position of the chars
# So in the above case, the permutation orders will be:
# acb => 132
# bac => 213
# bca => 231

# KEY: Only lower case letter => can be compare easily 
# KEY: IF it already the last => must return the first in order

# OBSERVATION
# The next permutation must only be created from the smallest possible increase in value from the original string (1) => Based on this, we must traverse from right to left since that's where the smallest place value is. (2)

# The largest permutation will always follow a non-increasing pattern (non-increasing since the next char in order could be equal to the one we are referencing). For example: cba => 321. There is no permutation of this string that could make it larger than the one we are referencing. From this we can deduce:
# KEY: To get the first in the permutation order (or the smallest one), we just need to reverse the string! (3)

# Now we traverse from right to left to try to find the smallest permutation possible (*2)
# We refer to the char that break the non-increasing order PIVOT and the existing suffix sub-string SUFFIX. 
# When moving, if the SUFFIX is non-increasing => That's already the largest permutation of said SUFFIX so nothing can be moved to make that smaller. That's conflicting with point (*1)
# But what happen when we are traversing and meet a char that break the non-increasing order (PIVOT)?
# We need to make the smallest possible INCREASE but the chars must only be changed position. (3)
# So now we also traverse the SUFFIX, find the one that is larger than PIVOT and switch place.

# Can we make the new string smaller? Yes, because the new SUFFIX is still in non-increasing order. Therefore, based on (*3), we reverse it than its or next lexicographical order.

# ORDER OF IMPLEMENTATION:
# 1 - Search for the pivot. If there is none satisfy the condition then reverse the string. 
# 2 - If there is, search the suffix for the one to replace.
# 3 - Replace then reverse the suffix.

# TIME: O(n) since we traverse the string once max
# SPACE: O(n) since we create a new list
def next_lexicographical_seq(s : str) -> str:
    chars = list(s)
    pivot = len(chars) - 2
    
    # If there is only one char, return itself?
    if len(chars) <= 1: return s
    
    # Search for PIVOT
    while pivot >= 0 and chars[pivot] >= chars[pivot + 1]:
        pivot -= 1
    
    # No pivot found, return reversed string
    if pivot == -1:
        chars.reverse()
        return ''.join(chars)
    
    search = len(chars) - 1
    # Search the SUFFIX for the one to be replace
    while chars[search] < chars[pivot]:
        search -= 1
        
    # When while break, that's when search is pointing at where its larger than where pivot is pointing
    chars[search], chars[pivot] = chars[pivot], chars[search]
    
    # Reverse to get the smallest permutation of SUFFIX
    chars[pivot + 1:] = reversed(chars[pivot + 1:])
            
    return ''.join(chars)

print(next_lexicographical_seq('ynitsed'))