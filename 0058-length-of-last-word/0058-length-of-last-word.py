class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        n  = len(s)
        if(len(s[n-1]) != 0 ):
            return len(s[n-1])
        else:
            return len(s[n-2])
        