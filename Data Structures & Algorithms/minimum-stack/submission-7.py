class MinStack:
    """
    a min stack support push, pop, top and getMin
    first 3 opera can use list
    getMin need other stack to store min to current
    also can use min_Val to store, but logic is way more complex
    """

    def __init__(self):
        self.min_stack = []
        self.stack =[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        else:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
        
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.min_stack[-1]
