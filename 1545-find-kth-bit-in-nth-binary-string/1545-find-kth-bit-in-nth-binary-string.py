class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            output = ""
            for i in s:
                if i == "0":
                    output += "1"
                else:
                    output += "0"
            return output
        
        def stringg(s):
            if s==1:
                return "0"
            
            return stringg(s-1) + "1" + invert(stringg(s-1))[::-1]
        
        return stringg(n)[k-1]
            
            
            