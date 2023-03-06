class MyStack:

    def __init__(self):
        self.queue1= []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        if len(self.queue1) == 0:
            self.queue1.append(x)
        else:
            for i in range(len(self.queue1)):
                self.queue2.append(self.queue1.pop(0))
            self.queue1.append(x)
            for j in range(len(self.queue2)):
                self.queue1.append(self.queue2.pop(0))
                
                
            
        

    def pop(self) -> int:
        return self.queue1.pop(0)
        
        

    def top(self) -> int:
        return self.queue1[0]
        

    def empty(self) -> bool:
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()