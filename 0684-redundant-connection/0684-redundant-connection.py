class UnionFind:
    def __init__(self, edges):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)
        for item in edges:
            self.parent[item[0]] = item[0]
            self.parent[item[1]] = item[1]
            self.rank[item[0]]= 0
            self.rank[item[1]] = 0
        
        
    def find(self, member):
        self.root = member
        while self.root != self.parent[self.root]:
            self.root = self.parent[self.root]

        while member != self.root:
            parent = self.parent[member]
            self.parent[member] = self.root
            member = parent

        return self.root
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    def check(self,x,y):
        if self.find(x) == self.find(y):
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(edges)
        for item in edges:
            if  uf.check(item[0],item[1]):
                return item
            uf.union(item[0],item[1])
            
        
            
        
        