
class Solution:
    def isUgly(self, n: int) -> bool:
        
        while n>0:
            if n==1:
                return True
            elif n%2 == 0:
                n/=2
            elif n%3 == 0:
                n/=3
            elif n%5 == 0:
                n/=5
            else:
                return False
            
      