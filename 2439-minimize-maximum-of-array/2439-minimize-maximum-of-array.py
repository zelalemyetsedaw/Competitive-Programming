class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        minimum = 0
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if nums[i] > minimum:
                minimum = max(minimum,(sum + i) // (i+1))
                
        return minimum
                
            