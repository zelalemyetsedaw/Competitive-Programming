class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largestSum = nums[0]
        
        cursum = 0
        
        for item in nums:
            
            if cursum < 0:
                cursum = 0
            
            cursum += item
            largestSum = max(largestSum,cursum)
            
        return largestSum