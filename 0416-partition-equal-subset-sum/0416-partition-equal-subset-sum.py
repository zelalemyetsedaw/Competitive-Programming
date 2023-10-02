class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        
        dp = [[-1] * (summ//2 + 1) for i in range(len(nums) + 1)]
        
        for i in range(len(nums) + 1):
            for s in range((summ//2)+1):
                if s == 0:
                    dp[i][s] = True
                elif i == 0:
                    dp[i][s] = False
                    
                elif nums[i-1] > s:
                    dp[i][s] = dp[i-1][s]
                else:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]
                    
        return dp[-1][-1]
                
        