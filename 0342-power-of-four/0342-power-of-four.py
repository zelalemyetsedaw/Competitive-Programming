class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def ispoweroffour(n):
            if n == 1:
                return True
            elif n < 1:
                return False
        
            return ispoweroffour(n/4)
            
        return ispoweroffour(n)
                