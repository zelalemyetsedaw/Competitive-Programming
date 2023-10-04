class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-i for i in nums]
        heapq.heapify(nums)
        answer = 0
        for i in range(k):
            answer = -heappop(nums)
            
        return answer
            