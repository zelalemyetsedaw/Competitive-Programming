class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return image
        
        R, C = len(image), len(image[0])
        old = image[sr][sc]   
        if old == newColor: return image  
        def dfs(i,j,old,new):
            if image[i][j] == old:
                image[i][j] = new
                if i-1 >= 0: dfs(i-1, j,old,new)
                if i+1 < R: dfs(i+1, j, old,new)
                if j-1 >= 0: dfs(i, j-1,old,new)
                if j+1 < C: dfs(i, j+1,old,new)

        dfs(sr, sc, old,newColor)
        return image