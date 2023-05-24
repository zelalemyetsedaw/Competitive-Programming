class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        q = deque()
        result = [[] for i in range(n)]
        
        in_degree = [0]*n
        traversal = [[] for i in range(n)]
        
        for (a,b) in edges:
            in_degree[b] += 1
            traversal[a].append(b)
        
        hashset = set()
        for i,x in enumerate(in_degree):
            if x == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for j in traversal[node]:
                in_degree[j] -= 1
                result[j].append(node)
                result[j] = list(set(result[j] + result[node]))
                if in_degree[j] == 0:
                    q.append(j)
                
        for i in result:
            i.sort()
        return result