class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for i in recipes:
            incoming[i] = 0
        for i in supplies:
            incoming[i] = 0
        
        for i in range(len(recipes)):
            
            incoming[recipes[i]] = len(ingredients[i])
            
        for j in range(len(ingredients)):
            for i in ingredients[j]:
                graph[i].append(recipes[j])
            
        todo = deque([])
        for index in incoming:
            if incoming[index] == 0:
                todo.append(index)
        
        answer = []
        
        while todo:
            current = todo.popleft()
            for child in graph[current]:
                incoming[child] -= 1
                
                
                if incoming[child] == 0:
                    answer.append(child)
                    todo.append(child)
                
        return answer
        