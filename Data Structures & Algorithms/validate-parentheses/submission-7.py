class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paris = {'}': '{', ']':'[', ')':'('}

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif not stack  or stack[-1] != paris[s[i]]:
                return False
            else:
                stack.pop()
        return not stack
