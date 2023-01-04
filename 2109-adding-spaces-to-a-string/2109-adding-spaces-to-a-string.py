class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        j = 0
        k=1
        for i in spaces:
            output += s[j:i] + " "
            j = i
        output += s[j:]
           
            
        return output