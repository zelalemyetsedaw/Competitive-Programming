class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        d = defaultdict(set)
        for item in roads:
            d[item[0]].add(item[1])
            d[item[1]].add(item[0])
            
        maxvalue = 0
        
        for i in d:
            for j in d:
                if j!=i:
                    if i in d[j]:
                        maxvalue = max(maxvalue,len(d[i]) + len(d[j])-1)
                    else:
                        maxvalue = max(maxvalue,len(d[i]) + len(d[j]))
        
        return maxvalue
                
            