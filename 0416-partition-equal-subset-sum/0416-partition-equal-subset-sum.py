class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        
        memo = [[-1] * (summ//2 + 1) for i in range(len(nums) + 1)]
        def recursion(summ,index):
            if memo[index][summ] != -1:
                return memo[index][summ]
            if summ == 0:
                return True
            if index == 0 or summ < 0:
                return False
            
            memo[index][summ] = recursion(summ,index - 1) or recursion(summ - nums[index - 1],index - 1)
            return memo[index][summ]
        
        return recursion(summ//2,len(nums))