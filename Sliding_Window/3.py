# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest

# without duplicate characters.



# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = {}
        l = 0
        maxLen = 0

        for r in range(len(s)):
            c = s[r]
            if c in charSet and charSet[c] >= l:
                l = charSet[c] + 1
            charSet[c] = r
            maxLen = max(maxLen, r-l+1)

        return maxLen


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
