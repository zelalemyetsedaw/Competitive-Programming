class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        
        output = []
        
        while columnNumber>0:
            columnNumber -= 1
            curr = columnNumber%26
            columnNumber = int(columnNumber/26)
           
            output.append(chr(curr + ord('A')))
            
        return "".join(output[::-1])
            
            
        