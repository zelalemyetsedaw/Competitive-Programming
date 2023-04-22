class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color = defaultdict(int)
        answer = set()
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour in color:
                    if color[neighbour] == color[node]:
                        answer.add(False)
                else:
                    color[neighbour] = 1 - color[node]
                    dfs(neighbour)
                     
            
            
        
        for node in graph:
            if node not in color:
                color[node] = 0
                dfs(node)
        
        if False in answer:
            return False
        else:
            return True
