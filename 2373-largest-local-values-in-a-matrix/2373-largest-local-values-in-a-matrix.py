class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(1,len(grid)-1):
            col = []
            for j in range(1,len(grid)-1):
                col.append(max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]))
            answer.append(col)
        return answer
                