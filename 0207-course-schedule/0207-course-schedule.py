class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i,j in prerequisites:
            graph[i].append(j)
            indegree[j] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            x = queue.popleft()
            
            for child in graph[x]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return sum(indegree) == 0