class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
       

    def push(self, val):
        
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)
            
        
        
        

    def pop(self):
        popped = self.stack.pop()
        if self.minstack[-1] == popped:
            self.minstack.pop()
        
        

    def top(self):
        return self.stack[-1]
        
        

    def getMin(self):
        return self.minstack[-1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()