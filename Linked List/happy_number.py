# In number theory, a happy number is defined as a number that, when repeatedly subjected to the process of squaring its digits and summing those squares, eventually leads to 1 [1]. An unhappy number will never reach 1 during this process, and will get stuck in an infinite loop.
# 
# Given an integer, determine if it's a happy number => return bool
# 
# Input: n = 23
# Output: True
# Explanation: 2² + 3² = 13 → 1² + 3² = 10 → 1² + 0² = 1

# Observation
# We use one number to get the next number. Does this sound familiar to a DS?
# That's right, its a linked list. Since the problem state that the process of doing this could stuck in an infinite loop. Does this sound familiar to you?
# That's also right, its the linked list loop finder problem!

# Small problem: How do we find the next number
# Num % 10 get the last digit
# Num / 10 get the remaining digits
# Stop when num / 10 = 0

# TIME: I don't know yet man. The book said its too complex. Damn.
# SPACE: O(1)
def next_number (num: int) -> int:
    nextNumber = 0
    remainDigits = num
    while remainDigits != 0:
        lastDigit = remainDigits % 10
        nextNumber = nextNumber + lastDigit ** 2
        remainDigits = remainDigits / 10
        
    return next_number

def happy_number (num: int) -> bool:
    slowPointer = num
    fastPointer = num
    while True:
        slowPointer = next_number(slowPointer)
        fastPointer = next_number(next_number(fastPointer))
        if fastPointer == 1:
            return True
        elif slowPointer == fastPointer:
            return False