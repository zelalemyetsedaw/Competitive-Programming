class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] 
        
            
        total = nums[len(nums)-1]
        
        
        for i in range(len(nums)):
            
            if i==0 and (total - nums[i]) == 0:
                return i
            elif i==0:
                continue
            elif nums[i-1] == total - nums[i]:
                return i
        return -1
    
    