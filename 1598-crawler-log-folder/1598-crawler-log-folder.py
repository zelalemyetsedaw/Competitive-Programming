class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        
        for item in logs:
            if (not stack and item == "../") or item == "./" :
                continue
            elif stack and item == "../":
                stack.pop()
            else:
                stack.append(item)
                
        return len(stack)
                