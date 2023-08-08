class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        sets = set()
        
        for i in range(22):
            sets.add(2 ** i)
            
        d = defaultdict(int)
        
        
        for item in deliciousness:
            d[item] += 1
        count = 0  
        
        for item in sets:
            for i in deliciousness:
                if (item-i) in d and (item-i) != i:
                    count += d[item-i]
                    
                elif (item-i) in d and (item-i) == i:
                    count += d[item-i] - 1 
                    
                    
        return (count//2) % (10**9 + 7)
        
        