class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(1,n-1):
            for j in range(1,m-1):
                
                array1 = [grid[i-1][j-1] , grid[i-1][j] , grid[i-1][j+1] , grid[i][j-1] , grid[i][j] , grid[i][j+1], grid[i+1][j-1] , grid[i+1][j] , grid[i+1][j+1]]
                array1.sort()
                
                if  array1!= [1,2,3,4,5,6,7,8,9]:
                    continue
                
                diagonal1 =  grid[i][j] + grid[i-1][j-1] + grid[i+1][j+1]
                diagonal2 = grid[i][j] + grid[i-1][j+1] + grid[i+1][j-1]
                row1 = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                row2 = grid[i][j-1] + grid[i][j] + grid[i][j+1]
                row3 = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                col1 = grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]
                col2 = grid[i-1][j] + grid[i][j] + grid[i+1][j]
                col3 = grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]
                if diagonal1 == diagonal2 == row1 == row2 == row3 == col1 == col2 == col3:
                    count += 1
                    
        return count 
                