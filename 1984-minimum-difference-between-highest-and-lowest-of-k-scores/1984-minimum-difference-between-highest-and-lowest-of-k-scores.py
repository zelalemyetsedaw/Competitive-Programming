class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = k-1
        
        nums.sort()
        mindifference = float("inf")
        while right < len(nums):
            
            mindifference = min(nums[right]-nums[left],mindifference)
            left += 1
            right += 1
            
        return mindifference
            