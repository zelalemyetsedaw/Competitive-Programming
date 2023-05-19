class UnionFind:
    
    def __init__(self, n):
        self.parent = [-1 for _ in range(len(n)+1)]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True
    
    def find(self, x):
        if self.parent[x] < 0:
            return x
        
        root = self.find(self.parent[x])
        self.parent[x] = root
        return root
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(edges)
        for start, end in edges:
            if uf.union(start, end) == False:
                return [start, end]