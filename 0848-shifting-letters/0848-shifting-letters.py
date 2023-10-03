class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        n = len(s)
        ans = ""
        
        
        for i in range(n-2,-1,-1):
            shifts[i] += shifts[i+1]
            
        for i in range(n):
            
            ans += chr((ord(s[i]) - 97 + shifts[i] ) % 26  + 97)
            
        return ans
            
            
        