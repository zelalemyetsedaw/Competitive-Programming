class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        stack=[]  # stack to store the indexes 
        stack.append(-1) 
        result=0 #to track the max size
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                stack.pop()
                if not stack: 
                    stack.append(i)  
                result=max(result,i-stack[-1])
        return result