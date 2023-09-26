class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        summ = sum(stones)
        half = ceil(summ/2)
        memo = defaultdict(int)
        def recursion(i,total):
            if (i,total) in memo:
                return memo[(i,total)]
            if i == len(stones) or total >= half:
                return abs(total - (summ - total))
            
            
            memo[(i,total)] = min(recursion(i+1,total),recursion(i+1,total + stones[i]))
            return memo[(i,total)]
        
        return recursion(0,0)
        