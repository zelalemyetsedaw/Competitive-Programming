class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
       
        visit = set()
        colorcheck = image[sr][sc]

        def dfs(row,col):
            
            if row >= len(image) or col >= len(image[0]) or row<0 or col<0 or image[row][col] != colorcheck or (row,col) in visit:
                return
            
            visit.add((row,col))
            image[row][col] = newColor
            
            dfs(row,col+1)
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)

        dfs(sr,sc)
        return image