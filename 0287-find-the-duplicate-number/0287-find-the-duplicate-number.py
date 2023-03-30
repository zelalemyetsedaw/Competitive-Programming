class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            temp = nums[i]
            
            if temp != nums[temp-1] and i+1 != temp:
                nums[i],nums[temp-1] = nums[temp-1],temp
                
            else:
                i += 1
                
            
            
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return nums[i]