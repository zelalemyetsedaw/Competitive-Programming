class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        
        if len(nums)==1:
            return nums[0]
        
        for item in nums[0:len(nums)-1]:
            temp = max(rob1+item,rob2)
            rob1 = rob2
            rob2 = temp
            
        max1 = rob2
        rob1 = 0
        rob2 = 0
        for item in nums[1:]:
            temp = max(rob1+item,rob2)
            rob1 = rob2
            rob2 = temp
            
        return max(max1,rob2)