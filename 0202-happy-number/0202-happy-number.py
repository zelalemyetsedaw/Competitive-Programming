class Solution:
    def isHappy(self, n: int) -> bool:
        sets = set()
        while n != 1:
            if n in sets: return False
            sets.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True