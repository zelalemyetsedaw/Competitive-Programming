class Solution:
    def decodeString(self, s: str) -> str:
        
        
        def helper(i,n,l):
            if i>=len(s):
                return ""

            if s[i]=="]":
                l[0] = i #we keep track where we left
                return ""

            if s[i]=="[":
                return int(n)*helper(i+1,"",l)+helper(l[0]+1,"",l)

            if s[i].isnumeric():
                return helper(i+1,n+s[i],l)

            else:
                return s[i]+helper(i+1,n,l)

        l = [0]
        return helper(0,"",l)