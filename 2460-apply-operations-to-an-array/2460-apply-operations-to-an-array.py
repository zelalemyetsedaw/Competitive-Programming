class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        
        left = 0
        right = 0
        
        while right < n and left < n:
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            if nums[left] != 0:
                left += 1
            
                
            right += 1
        return nums
