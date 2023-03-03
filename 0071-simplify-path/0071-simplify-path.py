class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currentstring = ""
        
        for item in path + "/":
            if item == '/':
                if currentstring == ".." and stack:
                    stack.pop()
                elif currentstring != "" and currentstring != "." and currentstring != "..":
                    stack.append(currentstring)
                currentstring = ""
                
                
            else:
                currentstring += item
                
        return "/" + "/".join(stack)
                
            