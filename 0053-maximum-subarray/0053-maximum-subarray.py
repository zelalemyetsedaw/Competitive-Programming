class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = nums[0]
        
        cursum = 0
        
        for item in nums:
            
            if cursum < 0:
                cursum = 0
            
            cursum += item
            largest = max(largest,cursum)
            
        return largest