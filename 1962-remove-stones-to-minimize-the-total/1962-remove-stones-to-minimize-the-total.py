class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        for item in piles:
            heappush(heap,-item)
            
        
        
        for i in range(k):
            x = heappop(heap)
            x = (-x - (-x//2))
            heappush(heap,-x)
            
        return -sum(heap)
        