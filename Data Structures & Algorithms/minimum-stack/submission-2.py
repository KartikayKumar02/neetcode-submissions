class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack == [] or val <= self.minstack[-1]: 
            self.minstack.append(val)
        

    def pop(self) -> None:
        top_element = self.stack[-1]
        self.stack.pop()
        if top_element == self.minstack[-1]:
            self.minstack.pop()
        
        
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]

        
