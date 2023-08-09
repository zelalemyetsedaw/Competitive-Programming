class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse=True)
        summ = 0
        left = 1
        right = len(piles)-1
        while left < right:
            summ += piles[left]
            left += 2
            right -= 1
            
            
        return summ
            
        