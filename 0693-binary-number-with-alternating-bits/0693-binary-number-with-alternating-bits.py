class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n))
        print(n)
        
        for i in range(3,len(n)):
            if n[i] == n[i-1]:
                return False
        return True
        