class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = 0
        for i in weights:
            right += i
        summ = 0
        capacity = 0
        
        while left < right:
            capacity = (left + right)//2
            count = 1
            summ = 0
            for i in weights:
                if summ +i > capacity:
                    count += 1
                    summ = 0
                summ += i
         
            if count > days:
                left = capacity + 1
               
            else:
                right = capacity 
                
        return left
            