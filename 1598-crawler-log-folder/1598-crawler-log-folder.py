class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for item in logs:
            if item == "../" and stack:
                stack.pop()
            elif item != "./" and item != "../":
                stack.append(item)
                
        return len(stack)
            