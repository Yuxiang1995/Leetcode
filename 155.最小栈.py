class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal:
            self.minVal.append(val)
        else:
            self.minVal.append(min(val, self.minVal[-1]))

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]
            del self.minVal[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]