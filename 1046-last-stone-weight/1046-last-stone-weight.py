class Solution:       
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s * -1 for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            remaining = abs(s2 - s1)
            heapq.heappush(stones, remaining * -1)
        
        return 0 if not stones else heapq.heappop(stones) * -1
        
            

        
        