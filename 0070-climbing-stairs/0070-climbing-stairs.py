class Solution:
    def climbStairs(self, n: int) -> int:
        
        d = defaultdict(int)
        d[1] = 1
        d[2] = 2
        
        def climb(n):
            if n<3:
                return n
            if n not in d:
                d[n] = climb(n-1) + climb(n-2)
                
            return d[n]
                
           
                
            
        return climb(n)
            