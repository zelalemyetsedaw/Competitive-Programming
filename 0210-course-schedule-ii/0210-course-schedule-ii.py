class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        answer = []        
        while queue:
            x = queue.popleft()
            answer.append(x)
            for child in graph[x]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(answer) != numCourses:
            return []
        return answer
            
        