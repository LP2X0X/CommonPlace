from typing import List

# KEY: Remove all non-alphanumeric character

# OBSERVATION: Perfect use of two pointer, using inward pointers, we can compare both characters from both end. If they match each other, we advance till left char index equal right char index, if not, we return false.
# OBSERVATION: In case the number of chars is even, then the above condition does not satisfy to stop. => Check for len of chars is even or not? No, it stop when left equal right or when left larger than right => Which also means it continue only when left less than right.
# OBSERVATION: To remove the non-alphanumeric in O(1) time, we can create a dict with all of them.

# TIME: O(n). Well acktually, it is O(n/2) but you know...
# SPACE: O(1) since we only allocate a constant number of variables
def is_palindrome_valid (s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # We can move freely here cause the index of non-alphanumeric chars is not respected
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# TEST CASES:
print(is_palindrome_valid(""))
print(is_palindrome_valid("a"))
print(is_palindrome_valid("aa"))
print(is_palindrome_valid("ab"))
print(is_palindrome_valid("!, (?)"))
print(is_palindrome_valid("hello, world!"))


# Personl implementation of isalnum
def isAlNum(c: str) -> bool:
    # Use set as a look up table for O(1) look up time and O(1) for space since there is only a constant number of variable being created
    alpha = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return c in alpha 
