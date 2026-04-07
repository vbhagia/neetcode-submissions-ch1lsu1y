class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack
        if len(self.minStack) == 0:
            self.minStack = [val]
        else:
            self.minStack = [min(val, self.minStack[0])] + self.minStack
            print(self.minStack) 

    def pop(self) -> None:
        self.minStack.pop(0)
        self.stack.pop(0)
        print(self.minStack)
        

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minStack[0]