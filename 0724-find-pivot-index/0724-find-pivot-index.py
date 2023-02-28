class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = [nums[0]]*len(nums)
        rightsum = [nums[len(nums)-1]] * (len(nums)+1)
        
        for i in range(1,len(nums)):
            leftsum[i] = leftsum[i-1] + nums[i]
        for i in range(len(nums)-2,-1,-1):
            rightsum[i] = rightsum[i+1] + nums[i]
            
        rightsum[len(nums)] = 0
        leftsum[-1] = 0
            
        for i in range(0,len(nums)):
            if leftsum[i-1] == rightsum[i+1]:
                return i
        return -1