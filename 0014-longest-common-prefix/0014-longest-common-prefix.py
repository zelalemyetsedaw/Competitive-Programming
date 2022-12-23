class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        else:
            prev = strs[0]
            lprev = len(prev)
            for i in strs[1:]:
                while prev!=i[0:lprev]:
                    prev = prev[0:(lprev-1)]
                    lprev -= 1
                
                if(lprev ==0):
                    return("")
        return prev
        