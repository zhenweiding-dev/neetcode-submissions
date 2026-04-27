class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        paris = {'}': '{', ']':'[', ')':'('}

        for i in s:
            if i in paris:
                if stack and stack[-1] == paris[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False