class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
                
        memo = {}
        
        def recursion(cursum,index):
       
            
            if index == len(nums):
                if cursum == target:
                    return 1
                return 0
            
            if (index,cursum) in memo:
                return memo[(index,cursum)]
            
            
            
            
            memo[(index,cursum)] = recursion(cursum + nums[index],index + 1) +                                                  recursion(cursum - nums[index] ,index+1)
            
            
            
            
            return memo[(index,cursum)]
            
       
        return recursion(0,0)
             