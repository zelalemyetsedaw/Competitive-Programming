class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        def recursion(summ,index):
            if (summ,index) in memo:
                return memo[(summ,index)]
            if summ == 0 and index == 0:
                return 1
            elif index == 0:
                return 0
            
            
            memo[(summ,index)] = recursion(summ-nums[index-1],index-1) + recursion(summ+nums[index-1],index - 1)
            return memo[(summ,index)]
        
        return recursion(target,len(nums))
                

             