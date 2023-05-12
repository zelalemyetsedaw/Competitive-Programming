class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for i,j in prerequisites:
            graph[j].append(i)
            incoming[i] += 1
            
        queue = deque([])
        
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
                
        answer = []
        while queue:
            x = queue.popleft()
            answer.append(x)
            for child in graph[x]:
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append(child)
                    
        return len(answer) == numCourses
            