class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
    
        dp = [[0] * n for _ in range(m)]

        # Base case: there is only one way to reach the bottom-right cell
        dp[m - 1][n - 1] = 1

        # Fill the last row (from right to left)
        for c in range(n - 2, -1, -1):
            dp[m - 1][c] = dp[m - 1][c + 1]

        # Fill the last column (from bottom to top)
        for r in range(m - 2, -1, -1):
            dp[r][n - 1] = dp[r + 1][n - 1]

        # Fill the rest of the cells using the recurrence relation
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        


    
        return dp[0][0]  

        
    