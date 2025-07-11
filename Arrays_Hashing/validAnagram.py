# Given two strings s and t, return true if t is an of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false



from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterT = Counter(t)
        counterS = Counter(s)

        for c in s:
            if counterS[c] != counterT[c]:
                return False

        return True
