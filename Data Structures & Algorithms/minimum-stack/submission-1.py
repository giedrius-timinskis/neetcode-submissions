class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack):
            currMin = self.minStack[-1]
            newVal = min(val, currMin)
            self.minStack.append(newVal)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
            self.minStack.pop()
        

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack):
            return self.minStack[-1]
