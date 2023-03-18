class StockSpanner:

    def __init__(self):
        self.stack = []
    
        

    def next(self, price: int) -> int:
        count = 1
        if not self.stack:
            self.stack.append([price,count])
        elif price < self.stack[-1][0]:
            self.stack.append([price,count])
        else:
            while self.stack and self.stack[-1][0] <= price:
                count += self.stack[-1][1]
                self.stack.pop()
                
                
            self.stack.append([price,count])
        
        return self.stack[-1][1]
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)