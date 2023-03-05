class DataStream:

    def __init__(self, value: int, k: int):
        self.deque = collections.deque()
        self.value = value
        self.k = k
        self.d = defaultdict(int)
        

    def consec(self, num: int) -> bool:
        self.deque.append(num)
        if self.value == num:
            self.d[num] += 1
        while len(self.deque) > self.k:
            x = self.deque.popleft()
            self.d[x] -= 1
            if self.d[x] == 0:
                self.d.pop(x)
        
        return self.k == self.d[num]
                
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)