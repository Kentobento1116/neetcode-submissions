class MinStack:

    def __init__(self):
        self.stack = []
        self.revOrdered = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.revOrdered[-1] if self.revOrdered else val)
        self.revOrdered.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.revOrdered.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.revOrdered[-1]
