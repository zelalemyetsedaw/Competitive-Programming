class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for item1 in range(len(bombs)):
            for item2 in range(len(bombs)):
                if item1 != item2:
                    if bombs[item1][2] >= math.sqrt((bombs[item2][0]-bombs[item1][0]) ** 2 + (bombs[item2][1]-bombs[item1][1]) ** 2):
                        graph[item1].append(item2)
        
        
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        
        maxvalue = 1
        
        for i in list(graph):
            visited  = set()
            dfs(i)
            maxvalue = max(maxvalue,len(visited))
                
        return maxvalue