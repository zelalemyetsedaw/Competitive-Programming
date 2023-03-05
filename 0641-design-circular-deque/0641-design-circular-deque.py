class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue = [] * k
        self.k = k
        self.length = 0
        

    def insertFront(self, value: int) -> bool:
        if self.k == self.length:
            return False
        else:
            self.dequeue.insert(0,value)
            self.length += 1
            return True
        

    def insertLast(self, value: int) -> bool:
        if self.k == self.length:
            return False
        else:
            self.dequeue.append(value)
            self.length += 1
            return True
        

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.dequeue.pop(0)
            self.length -= 1
            return True
        

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.dequeue.pop()
            self.length -= 1
            return True
        

    def getFront(self) -> int:
        if self.length == 0:
            return -1
        else:
            return self.dequeue[0]
        

    def getRear(self) -> int:
        if self.length == 0:
            return -1
        else:
            return self.dequeue[-1]
        

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.length == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()