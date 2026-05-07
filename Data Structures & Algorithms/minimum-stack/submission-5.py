class MinStack:
    # use a min_val to track current min_val
    # use val - minval to store actual val
    # use min_val negative as a sign of min change
    # when pop negative val, restore min_val
    
    def __init__(self):
        self.min_val = float('inf')
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val

        self.stack.append(val - self.min_val)

        self.min_val = min(self.min_val, val)
        
    def pop(self) -> None:
        if self.stack[-1] < 0:
            self.min_val -= self.stack[-1]
        
        self.stack[-1] += self.min_val
        
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_val
        return self.stack[-1] + self.min_val
        

    def getMin(self) -> int:
        return self.min_val
        
