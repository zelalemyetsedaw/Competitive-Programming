class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i< len(nums):
            temp = nums[i]
            if nums[i] != len(nums) and nums[i] != i  :
                nums[i],nums[temp] = nums[temp],temp
                
            else:
                i += 1
                
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return len(nums)

                
                
       