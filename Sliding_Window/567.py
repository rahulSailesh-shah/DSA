# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a
# of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def updateMatches(newFreq, oldFreq, charIdx):
            nonlocal matches
            if newFreq == s1Count[charIdx]:
                matches += 1
            if oldFreq == s1Count[charIdx]:
                matches -= 1

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        l = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[i]) - ord('a')
            oldFreq = s2Count[idx]
            s2Count[idx] += 1
            newFreq = s2Count[idx]
            updateMatches(newFreq, oldFreq, idx)

            idx = ord(s2[l]) - ord('a')
            oldFreq = s2Count[idx]
            s2Count[idx] -= 1
            newFreq = s2Count[idx]
            updateMatches(newFreq, oldFreq, idx)

            l += 1

        return matches == 26


print(Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo"))
