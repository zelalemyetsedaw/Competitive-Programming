class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for item in adjacentPairs:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])
        
        start = 0
        for item in graph:
            if len(graph[item]) == 1:
                start = item
                
        queue = deque([start])
        answer = [start]
        visited = set([start])
        while queue:
            x = queue.popleft()
            for item in graph[x]:
                if item not in visited:
                    answer.append(item)
                    visited.add(item)
                    queue.append(item)
        
        return answer