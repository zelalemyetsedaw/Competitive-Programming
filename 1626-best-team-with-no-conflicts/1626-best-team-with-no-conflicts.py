class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        agescores = []
        n = len(scores)
        for i in range(n):
            agescores.append((ages[i],scores[i]))
            
        agescores.sort()
        memo = [[-1] * (n+2) for _ in range(n+2)]
        
        def recursion(prev_index,cur_index):
            if memo[prev_index][cur_index] != -1:
                return memo[prev_index][cur_index]
            if cur_index >= n:
                return 0
            
            pick,notpick = 0,0
            if prev_index == -1 or agescores[cur_index][1] >= agescores[prev_index][1]:
                pick = agescores[cur_index][1] + recursion(cur_index,cur_index + 1)
            notpick = 0 + recursion(prev_index,cur_index + 1)
            
            memo[prev_index][cur_index] = max(pick,notpick)
            return max(pick,notpick)
        
        return recursion(-1,0)
                
                    
                
                