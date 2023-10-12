class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        d2 = defaultdict(int)
        for j in t:
            d2[j] += 1
            
        return d == d2
            
        