class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        answer = [0] * len(labels)
        
        
        
        def dfs(temp,prev):
            count = Counter()
            label = labels[temp]
            count[label] = 1
            
            for child in graph[temp]:
                if child == prev:
                    continue
                
                count += dfs(child,temp)
                
            
                
            answer[temp] = count[label]
            return count
                
                
                
                 
        dfs(0,None)
       
        return answer
                
            