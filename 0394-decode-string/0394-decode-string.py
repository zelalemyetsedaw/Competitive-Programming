class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        numstack = []
        stack = []
        temp = ""
        num = ""
        for i in  range(len(s)):
            if s[i].isdigit():
                num += s[i]
                if not s[i+1].isdigit():
                    numstack.append(int(num))
                    num = ""
            elif s[i] == "]":
                i = s[i]
                while i != "[":
                    temp = stack.pop() + temp
                    i = stack[-1]
                stack.pop()
                temp = temp * int(numstack.pop())
                
                if not numstack:
                    output = output + "".join(stack)  + temp
                    stack = []
                    temp = ""
                else:
                    stack.append(temp)
                    temp = ""
                    
                
                    
            else:
                stack.append(s[i])
        
                
                
        return output + "".join(stack)
                
            