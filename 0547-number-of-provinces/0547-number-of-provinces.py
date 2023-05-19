class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        x = 202
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    
                    graph[i].append(j)
                    graph[j].append(i)
                    
        components = {}
        
        for city in graph:
            components[city] = set([city])
        
        
        for city in graph:
            for neighbor in graph[city]:
                if components[city] is not components[neighbor]:
                    components[city] |= components[neighbor]
                    
                    for c in components[neighbor]:
                        components[c] = components[city] # set references

       
        answer = set()
        for i in components.values():
            answer.add(tuple(i))
                
        return len(answer)
            
                
        

            