class DataStream:

    def __init__(self, value: int, k: int):
        self.deque = collections.deque()
        self.value = value
        self.k = k
        self.count = 0
        

    def consec(self, num: int) -> bool:
        self.deque.append(num)
        if self.value == num:
            self.count += 1
        while len(self.deque) > self.k:
            x = self.deque.popleft()
            if x == self.value:
                self.count -= 1
        
        return self.k == self.count
                
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)