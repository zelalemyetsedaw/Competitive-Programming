class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxperimeter = 0
        n = len(nums)
        for i in range(n-2):
            if(nums[i]+nums[i+1]>nums[i+2]):
                maxperimeter = max(maxperimeter,nums[i] + nums[i+1] + nums[i+2])
            
                
            
        return maxperimeter