class Solution:
    def myAtoi(self, s: str) -> int:
        stack = ['0']
        flag = ""
        for char in s:
            if len(stack)>1 and not char.isdigit() or (flag and not char.isdigit()):
                break
            if char != " " and char != "+" and char != "-" and not char.isdigit():
                break
            elif (char == "-" or char == "+") and flag or ((char == "-" or char == "+") and len(stack)>1):
                break
            if char == "-" or char == "+":
                flag = char
            elif char != " " and ord(char) >= 48 and ord(char) <= 57 :
                stack.append(char)
            
            
            
        result =  int("".join(stack))
        if flag == "-": result = -result
        maxx = (2 ** 31)-1
        minn = -(2 ** 31)
        if result > maxx:
            result = maxx
        if result < minn:
            result = minn
        return result
                
        