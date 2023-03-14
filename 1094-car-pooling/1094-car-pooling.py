class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lists = []
        for n, start, end in trips:
            lists.append((start, n))
            lists.append((end, -n))
            
        
        lists.sort()
        
        passanger = 0
        flag = True
        for item in lists:
            passanger += item[1]
            if passanger > capacity:
                flag = False
                
        return flag
            