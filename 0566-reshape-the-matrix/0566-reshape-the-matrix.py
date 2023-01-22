class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat) ,len(mat[0])
        if m*n !=  r*c: return mat
        
        output = [[0 for i in range(c)] for j in range(r)]
        k= 0
        for i in range(m):
            for j in range(n):
                output[k//c][k%c] = mat[i][j]
                k+=1
        return output