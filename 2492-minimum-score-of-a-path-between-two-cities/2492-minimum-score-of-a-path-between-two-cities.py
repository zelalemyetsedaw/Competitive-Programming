class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        big = float('inf')
        p, rank = list(range(n)), [big] * n

        def find(i):
            while i != p[i]:
                i = p[i]
            return i

        def union(i, j, dist):
            i, j = find(i), find(j)
            p[min(i, j)] = max(i, j)
            rank[i] = rank[j] = min(rank[i], rank[j], dist)

        for a, b, d in roads:
            union(a-1, b-1, d)

        return rank[find(0)]