class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        s = bin(int(str(n)))
        
        for i in s:
            if i == '1':
                count += 1
                
        return count
            