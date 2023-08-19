class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        temp = [0] * 1001
        
        for num,fromi,toi in trips:
            temp[fromi] += num
            temp[toi] -= num
        for i in range(1,len(temp)):
            temp[i] += temp[i-1]
            
        for item in temp:
            if item > capacity:
                return False
        return True
            