class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        top = 0
        left = 0
        down = n-1
        right = m-1
        direction = 0
        output = []
        while (left<=right and top<=down):
            if(direction==0):
                for i in range(left,right+1):
                    output.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top,down+1):
                    output.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    output.append(matrix[down][i])
                down -= 1
            elif direction == 3:
                for i in range(down,top-1,-1):
                    output.append(matrix[i][left])
                left += 1
            direction += 1
            direction %= 4
        return output
            