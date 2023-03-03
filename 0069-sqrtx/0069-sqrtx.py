class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        mid = 0
        if x==1:
            return 1
        while low < high:
            mid = low + (high-low)//2
            
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                low = mid+1
            else:
                return mid
            
        if mid * mid > x:
            return mid-1
        else:
            return mid
                