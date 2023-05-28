class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        def dfs(node, parent):
            totalTime = 0 
            for neigh in adj[node]:
                
                if neigh == parent: 
                    continue
                childTime = dfs(neigh, node)
                if hasApple[neigh] or childTime:
                    totalTime += (childTime+2)
            return totalTime
        
        
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        return dfs(0,-1)