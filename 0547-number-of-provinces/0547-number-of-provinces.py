class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        temp = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and i!= j:
                    temp[i].append(j)
            if i not in temp:
                temp[i].append(-1)
                    
        visited = set()            
        def dfs(city):
            
            visited.add(city)
            for item in temp[city]:
                if item != -1 and item not in visited:
                    dfs(item)
                    
        count = 0           
        for i in temp:
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
            