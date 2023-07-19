class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1,rob2 = 0,0
        
        for item in nums:
            temp = max(rob1+item,rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2