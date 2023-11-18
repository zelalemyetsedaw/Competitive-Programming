class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        graph = defaultdict(list)
        for i in range(n):
            first,second = equations[i]
            graph[first].append((second,values[i]))
            graph[second].append((first, 1 / values[i]))

        def bfs(src,target):
            if src not in graph or target not in graph:
                return -1
            
            visited = set()
            queue = deque([[src,1]])
            visited.add(src)
            while queue:
                x,w = queue.popleft()
                if x == target:
                    return w

                for child,weight in graph[x]:
                    if child not in visited:
                        queue.append([child,weight * w])
                        visited.add(child)
            return -1


        ans = []
        for x,y in queries:
            ans.append(bfs(x,y))

        return ans
                    




        