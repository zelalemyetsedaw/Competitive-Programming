class UnionFind:
    def __init__(self, equations):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)
        for item in equations:
            self.parent[item[0]] = item[0]
            self.parent[item[3]] = item[3]
            self.rank[item[0]]= 0
            self.rank[item[3]] = 0
        
        
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(equations)
        for item in equations:
            if item[1] == "=" and item[2] == "=":
                uf.union(item[0],item[3])
        for item in equations:
            if item[1] == "!" and item[2] == "=":
                if uf.check(item[0],item[3]):
                    return False
        return True
