class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for item in edges:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])
        n = len(d)
        for k in d:
            if len(d[k])==n-1:
                return k
            