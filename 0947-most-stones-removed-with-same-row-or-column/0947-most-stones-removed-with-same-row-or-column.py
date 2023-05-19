class UnionFind:
    def __init__(self, stones):
        self.parent = {}
        self.rank = defaultdict(lambda:1)
        for item in stones:
            self.parent[tuple(item)] = tuple(item)
           
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

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(stones)
        n = len(stones)
        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(tuple(stones[i]),tuple(stones[j]))
                    
        components = 0
        
        for item in uf.parent:
            if item == uf.parent[item]:
                components += 1
        return n- components
        
        
                    
        