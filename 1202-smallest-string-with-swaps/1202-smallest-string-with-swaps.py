class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = defaultdict(lambda: 0)
        
           
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
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for a,b in pairs:
            uf.union(a,b)
        for a,b in pairs:
            uf.find(a)
            uf.find(b)
        
        
        d = defaultdict(list)
        chars = defaultdict(list)
        
        for child,parent in uf.parent.items():
            chars[parent].append(s[child])
            
        
        for child,parent in uf.parent.items():
            d[parent].append(child)
        for item in d.values():
            item.sort() 
        for item in chars.values():
            item.sort()
       
        answer = [0] * n
        for item in d:
            j = 0
            for i in d[item]:
                answer[i] = chars[item][j]
                j+=1
        ans = ""        
        for i in answer:
            ans += i
            
        return ans
            
        