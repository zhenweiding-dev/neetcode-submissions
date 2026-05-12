class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        i tokens:[str] -> expression in reverse po n
        o return result (int)
        c may exist pority; operator in [+, -, *, /]; truncate to 0
        e
        use a new stack to mutipulte the computing process
        """
        res = []
        for op in tokens:
            if op not in ['+', '-', '*', '/']:
                res.append(int(op))
            else:
                right = res.pop()
                left = res.pop()
                if op == '+':
                    left += right
                elif op == '-':
                    left -= right
                elif op == '*':
                    left *= right
                else:
                   left = int(float(left) / right)
                res.append(left)
        return res[0]


        