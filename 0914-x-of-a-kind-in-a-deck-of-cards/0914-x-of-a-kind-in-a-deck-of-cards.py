class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        count = list(collections.Counter(deck).values())
        if len(count) == 1:
            return count[0] > 1
        gcds = gcd(count[0],count[1])
        for i in range(2,len(count)):
            gcds = gcd(gcds,count[i])
        
        return gcds > 1
        