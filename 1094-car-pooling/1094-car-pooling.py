class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
       
        
        array = [0] * 1002
        for num,fromm,to in trips:
            array[fromm] += num
            array[to ] -= num
            
        for i in range(1002):
            array[i] += array[i-1]
            
        for i in array:
            if i>capacity:
                return False
        return True
            