class Solution:       
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(stones)
        while len(stones)>1:
            n = len(stones)
            
            a,b = heapq.nlargest(2,stones)
            stones = heapq.nsmallest(n-2, stones)
            if a-b != 0:
                stones.append(a-b)
                heapify(stones)
        if not stones:
            return 0
        return stones[0]
            

        
        