class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        left = 1
        right = maxk
        res = maxk
        
        while left <= right:
            k = (left + right)//2
            summ = 0
            for i in range(len(piles)):
                summ += math.ceil(piles[i]/k)
            if summ <= h:
                res = min(k,res)
                right = k-1
            elif summ > h:
                left = k+1
            
                
        return res