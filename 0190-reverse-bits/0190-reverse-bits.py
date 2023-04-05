class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)
        print(n)
        n=n[::-1][:len(n)-2]
        n = "0b" + n + (32-len(n))*"0"
        
        return int(n,2)