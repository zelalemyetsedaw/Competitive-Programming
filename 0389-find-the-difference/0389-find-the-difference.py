class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(0,len(t)):
            if s == '': return t[i]
            elif t[i] in s:
                s = s.replace(t[i],'',1)
            else:
                return t[i]
                