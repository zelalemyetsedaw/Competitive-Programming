class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        left = 0
        right = len(matrix[0])-1
        down = len(matrix)-1
        answer = []
        direction = 0
        while left <= right and top <= down:
            if direction == 0:
                for i in range(left,right+1):
                    answer.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top,down+1):
                    answer.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    answer.append(matrix[down][i])
                down -= 1
            else:
                for i in range(down,top-1,-1):
                    answer.append(matrix[i][left])
                left += 1
            
            direction += 1
            direction %= 4

        return answer