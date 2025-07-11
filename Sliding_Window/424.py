# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        maxLen = 0
        maxFreq = 0

        for r in range(len(s)):
            c = s[r]
            charMap[c] = charMap.get(c, 0) + 1
            maxFreq = max(maxFreq, charMap[c])

            if (r-l+1) - maxFreq > k:
                charMap[s[l]] -= 1
                l += 1
            else:
              maxLen = max(maxLen, (r-l+1))

        return maxLen


print(Solution().characterReplacement(s = "ABAB", k = 2))
print(Solution().characterReplacement(s = "AABABBA", k = 1))
print(Solution().characterReplacement(s = "BAAAAAAAAAB", k = 2))
