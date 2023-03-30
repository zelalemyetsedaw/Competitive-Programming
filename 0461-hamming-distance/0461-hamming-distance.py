class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x ^ y))
        c = 0
        for i in x:
            if i == '1':
                c += 1
                
        return c
        