# 22. Generate Parentheses


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backTrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append('(')
                backTrack(open+1, close)
                stack.pop()

            if close < open:
                stack.append(')')
                backTrack(open, close+1)
                stack.pop()

        backTrack(0, 0)
        return res

print(Solution().generateParenthesis(n=1))
