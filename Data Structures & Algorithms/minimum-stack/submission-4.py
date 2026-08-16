class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.minElement.append(val)
        if val <= self.minElement[-1]:
            self.minElement.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minElement[-1]:
            self.minElement.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minElement:
            return self.minElement[-1]
        else:
            return None
