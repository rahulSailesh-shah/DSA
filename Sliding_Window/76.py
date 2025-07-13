# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window
# of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from typing import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
        counterS = {}
        have = 0
        need = len(counterT)

        resLen = float("inf")
        res = [-1, -1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            counterS[c] = counterS.get(c, 0)+ 1

            if c in counterT and counterS[c] == counterT[c]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]

                counterS[s[l]] -= 1
                if s[l] in counterT and counterT[s[l]] > counterS[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""


print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
