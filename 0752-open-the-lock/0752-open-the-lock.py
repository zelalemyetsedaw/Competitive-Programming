class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)
        queue = deque([(0, "0000")])
        
        if "0000" in visited:
            return -1
        
        while queue:
            steps, code = queue.popleft()
            
            if code == target:
                return steps
            
            for i in range(4):
                d = int(code[i])
                
                for k in (d-1)%10, (d+1)%10:
                    cand = code[:i] + str(k) + code[i+1:]
                    if cand not in visited: 
                        visited.add(cand)
                        queue.append((steps+1, cand))

        return -1