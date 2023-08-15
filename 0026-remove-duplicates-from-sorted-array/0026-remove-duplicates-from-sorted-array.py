class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        num = nums[0]
        count = 0
        for i in range(1,len(nums)):
            if num == nums[i]:
                nums[i] = 101
                count += 1
            else:
                num = nums[i]
            
        nums.sort()
        return len(nums) - count
        
        