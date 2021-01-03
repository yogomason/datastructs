class Stack:

    def __init__(self):
        
        self.stack = []

    def pop(self) -> int:
        return self.stack.pop()
    
    def push(self, val) -> bool:
        if val is None:
            return False
        self.stack.append(val)
        return True

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.pop())