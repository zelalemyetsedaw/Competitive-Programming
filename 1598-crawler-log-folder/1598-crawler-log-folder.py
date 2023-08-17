class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        
        for item in logs:
            if item == "../" and stack:
                stack.pop()
            elif item == "./" or (item == "../" and not stack):
                continue
            else:
                stack.append("x")
                
        return len(stack)
                