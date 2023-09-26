class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        r,c = len(dungeon) - 1 , len(dungeon[0]) - 1
        memo = defaultdict(int)
        
        def recursion(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if (i,j) == (r,c):
                return max(1,1-dungeon[i][j])
            if i > r or j > c:
                return float("inf")
            
            right = recursion(i,j+1)
            down = recursion(i+1,j)
            
            memo[(i,j)] =  max(1,min(right,down) - dungeon[i][j])
            return memo[(i,j)]
        
        return recursion(0,0)
            