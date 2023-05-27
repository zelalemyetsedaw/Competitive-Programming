class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        queue = deque([node for node in range(n) if len(graph[node]) == 1])
        while queue and len(graph) > 2:
            for _ in range(len(queue)):
                leaf = queue.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    queue.append(neighbor)
                del graph[leaf]
        
        return graph.keys()
                              

            