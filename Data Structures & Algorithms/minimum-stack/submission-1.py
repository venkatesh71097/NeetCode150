class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # self.stack.append(val)
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val) 

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        # tmp = []
        # min_val = self.stack[-1]
        # while len(self.stack):
        #     min_val = min(min_val, self.stack[-1])
        #     tmp.append(self.stack.pop())
        # while len(tmp):
        #     self.stack.append(tmp.pop())
        # return min_val
