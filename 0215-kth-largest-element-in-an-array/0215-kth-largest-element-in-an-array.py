class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heappush(heap,-i)
        
        maximum = 0
        for i in range(k):
            maximum = heappop(heap)
            
        return -maximum
            