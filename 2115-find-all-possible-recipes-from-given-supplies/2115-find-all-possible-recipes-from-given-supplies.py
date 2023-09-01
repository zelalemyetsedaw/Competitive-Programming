class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(recipes)):
            for j in ingredients[i]:
                graph[j].append(recipes[i])
                indegree[recipes[i]] += 1
                
        queue = deque()
        for i in supplies:
            queue.append(i)
        
        answer = []
        while queue:
            x = queue.popleft()
            
            for child in graph[x]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    answer.append(child)
                    
        return answer