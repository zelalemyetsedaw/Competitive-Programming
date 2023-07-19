class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        def backtrack(r,c):
            if r == m-1 and c== n-1:
                return 1
            if r < 0 or c < 0 or r==m or c==n:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = backtrack(r,c+1) + backtrack(r+1,c)
            
            return memo[(r,c)]
        
        return backtrack(0,0)
        
    