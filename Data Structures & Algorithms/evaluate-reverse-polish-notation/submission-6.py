class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        i tokens:[str] -> expstacksion in reverse po n
        o return stackult (int)
        c may exist pority; tokenerator in [+, -, *, /]; truncate to 0
        e
        use a new stack to mutipulte the computing process
        """
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    left += right
                elif token == '-':
                    left -= right
                elif token == '*':
                    left *= right
                else:
                   left = int(left / right)
                stack.append(left)
        return stack.pop()


        