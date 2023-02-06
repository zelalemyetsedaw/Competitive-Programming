class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 1
        if len(nums)==1:
            return nums[0]
        while left<len(nums):
            if left == len(nums)-1:
                return nums[left]
            if nums[left] != nums[right]:
                return nums[left]
            else:
                left+=2
                right +=2
            
                