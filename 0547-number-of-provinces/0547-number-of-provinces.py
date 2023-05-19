class Solution:
    
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.treeSize = [1 for _ in range(n)]
            self.count = n
        
        def union(self, a: int, b: int):
            a = self._find(a)
            b = self._find(b)
            if a == b:
                return
            if self.treeSize[a] < self.treeSize[b]:
                self.parent[a] = b
                self.treeSize[b] += self.treeSize[a]
            else:
                self.parent[b] = a
                self.treeSize[a] += self.treeSize[b]
            self.count -= 1
    
        def _find(self, x: int) -> int:
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
			

        def isConnected(self, a: int, b: int) -> bool:
            a = self._find(a)
            b = self._find(b)
            return a == b
    
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0 or len(isConnected[0]) == 0:
            return 0
        lenY, lenX = len(isConnected), len(isConnected[0])
        uf = self.UnionFind(lenY)
        cities = lenY
        for y in range(lenY):
            for x in range(y + 1, lenX):
                if isConnected[y][x] == 1:
                    uf.union(y, x)
        return uf.count