class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 1
        sets = set([0])
        while i**2 <= 2**31 -1:
            sets.add(i**2)
            i += 1
        for i in sets:
            if (c - i) in sets:
                return True
        return False