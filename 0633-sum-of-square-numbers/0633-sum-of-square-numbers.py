class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            sum = left ** 2 + right ** 2
            if sum == c:
                return True
            elif sum < c:
                left += 1
            else:
                right -= 1
        return False