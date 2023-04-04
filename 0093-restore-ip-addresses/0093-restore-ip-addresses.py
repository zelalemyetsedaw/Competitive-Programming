class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        if len(s) > 12:
            return answer
        
        def backtracking(i,dots,temp):
            if dots == 4 and len(s)==i:
                answer.append(temp[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i,min(len(s),i+3)):
                if int(s[i:j+1]) <= 255 and (i==j or s[i] != '0'):
                    backtracking(j+1,dots+1,temp + s[i:j+1] + ".")
            
            
        backtracking(0,0,"")
        return answer