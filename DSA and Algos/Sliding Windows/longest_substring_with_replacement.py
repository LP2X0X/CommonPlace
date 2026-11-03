# Longest Uniform Substring After Replacements
#
# A uniform substring is one in which all characters are identical. Given a string, determine the
# length of the longest uniform substring that can be formed by replacing up to k characters.
#
# Example:
#
#     c   c
# a a b c d c c a  ->  a a c c c c c a
#                          ^^^^^^^^^ longest uniform substring
#
# Input: s = "aabcdcca", k = 2
# Output: 5
#
# Explanation: if we can only replace 2 characters, the longest uniform substring we can
# achieve is "ccccc", obtained by replacing b and d with c.


# OBSERVATION:
# When running the string through our mind, we always try to find the most frequent character in it then we check the number of different char that can be replace equals k.
# => The minimum number of replacements needed to achieve uniformity is obtained by replacing all characters except the most frequent one in a string. (1)
#
# In other words:
# The window may only grow while its length is at most highest_freq + k. Call that number the limit. That can be represent by this formula: window_length = max_freq_of_char + k
#   - highest_freq is a record: the highest count any one character has reached in the window so far. That's why it never has to go down. And we can not change k.
#   - The hash map (freqs) is exact for the current window, so max(freqs.values()) would give the current window's real top count. The algorithm never needs it. Each step it reads only freqs[s[right]], because adding a character raises only that character's count, so only it can beat the record.
# PSEUDO CODE:
# num_chars_to_replace = string_len - most_frequent_count
#   If num_chars_to_replace <= k => This string is valid
#   If num_chars_to_replace > k => This string is invalid
# To find the most_frequent_countain a string, we can use hash map:
# For example: a b b c
# PSEUDO CODE:
# most_frequent_count = max(most_frequent_count, freq_map[a]) = 1
# most_frequent_count = max(most_frequent_count, freq_map[b]) = 1
# most_frequent_count = max(most_frequent_count, freq_map[b]) = 2
# most_frequent_count = max(most_frequent_count, freq_map[c]) = 2

# But that apply to string, what about a substring?
# For example: a a b c d c c a | With k = 2
# We know that sliding window technique work for substring problem...
# Iteration: a
#                    => Max_Freq = max(Max_Freq, Map[a]) = 1
#                    => Map {a : 1}
# Iteration: a a
#                    => Max_Freq = max(Max_Freq, Map[a]) = 2
#                    => Map {a : 2}
# Iteration: a a b
#                    => Max_Freq = max(Max_Freq, Map[b]) = 2
#                    => Map {a : 2, b = 1}
# Iteration: a a b c
#                    => Max_Freq = max(Max_Freq, Map[c]) = 2
#                    => Map {a : 2, b = 1, c = 1}
# Now number of chars to replace is 2 since the window length is 4 and the max_freq is 2
# So currently the longest length of satisfy substring is 4
# Iteration: a a b c d
#                    => Max_Freq = max(Max_Freq, Map[d]) = 2
#                    => Map {a : 2, b = 1, c = 1, d = 1}
# What do we do when the window needs more than k replacements?
# If the window_length is 4, then the current best window length of a substring is 4. Therefore, if we try to reduce the window_length, it does not have a logical meaning at all.
# That mean, we should only looking for the next larger window_length (this is also the length of the valid substring that we are looking for). But max_freq_of_char = window_length - k. With the next value of window_length is 5, we should be looking for max_freq_of_char of a character exist in the new substring 3 time. This also mean that max_freq_of_char is a global like value which represent the current best of all substring.
# Then, we must slide the window to find it. This happen when the number of char need replacements is larger than k. We do this by increasing the left pointer of the window. If its <=k then we increase the right pointer to increase the window size only.


# TIME: O(n)
# SPACE: O(m) for the map
def longest_uniform_substring_after_replacements(source: str, k: int) -> int:
    maxLen = 0
    srcLen = len(source)
    if srcLen == 0 or srcLen == 1:
        return srcLen

    # Only do this shit when the right side is value
    left = right = 0
    charMap = {}
    max_freq_of_char = 0
    while right < srcLen:
        rightChar = source[right]
        charMap[rightChar] = charMap.get(rightChar, 0) + 1
        max_freq_of_char = max(max_freq_of_char, charMap[rightChar])
        # Since max_freq_of_char value can only go up (and frankly we only care the case when it goes up) so even though max_freq_of_char can be stale and make num_chars_to_replace wrong, it does not affect our algo since that case is throw away any way.
        # This is based on the logic, the stale case happen cause we use max function. It is like saying, we only care about the max value so...
        num_chars_to_replace = (right - left + 1) - max_freq_of_char

        if num_chars_to_replace > k:
            charMap[source[left]] -= 1
            left += 1

        maxLen = right - left + 1
        right += 1

    return maxLen
