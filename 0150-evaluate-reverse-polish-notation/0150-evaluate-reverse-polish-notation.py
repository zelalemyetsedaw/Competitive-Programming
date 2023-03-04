class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "*" or item == "+" or item == "-" or item == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if(item == "*"):
                    stack.append(num1 * num2)
                elif(item == "+"):
                    stack.append(num1 + num2)
                elif(item == "-"):
                    stack.append(num2 - num1)
                elif(item == "/"):
                    stack.append(int(float(num2)/num1) )
                    
                
            else:
                stack.append(int(item))
                
        return stack[0]