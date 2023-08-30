class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        for nod1 , nod2 in redEdges:
            redGraph[nod1].append(nod2)
        for nod1 , nod2 in blueEdges:
            blueGraph[nod1].append(nod2)
            
        queue = deque()
        queue.append([0,0,None])
        answer = [-1] * n
        visited = set((0,None))
        
        while queue:
            node,distance,color = queue.popleft()
            if answer[node] == -1:
                answer[node] = distance
            if color != "RED":
                for r in redGraph[node]:
                    if (r,"RED") not in visited:
                        queue.append([r,distance+1,"RED"])
                        visited.add((r,"RED"))
            if color != "BLUE":
                for r in blueGraph[node]:
                    if (r,"BLUE") not in visited:
                        queue.append([r,distance+1,"BLUE"])
                        visited.add((r,"BLUE"))
        return answer
            