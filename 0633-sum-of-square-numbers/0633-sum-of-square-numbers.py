class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        flag = False
        while left<=right:
            if left**2 + right**2 == c:
                flag = True
                break
            elif left**2 + right**2 > c:
                right -=1
            else:
                left += 1
        return flag