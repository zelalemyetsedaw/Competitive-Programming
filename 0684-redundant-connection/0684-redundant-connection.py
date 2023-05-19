class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]

        def find(n):
            p = par[n]

            while p != par[p]:
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[n1] > rank[n2]:
                rank[n1] += rank[n2]
                par[p2] = par[p1]

            else:
                rank[n2] += rank[n1]
                par[p1] = par[p2]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]