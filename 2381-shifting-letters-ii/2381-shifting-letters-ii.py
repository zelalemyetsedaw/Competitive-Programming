class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        array = [0] * (len(s) + 1)
        for a,b,c in shifts:
            if c == 0:
                array[a] += -1
                array[b+1] += 1
            elif c==1:
                array[a] += 1
                array[b+1] -= 1
                
        for i in range(1,len(array)):
            array[i] += array[i-1]
        
        ans = list(s)
        
       
        for i in range(len(s)):
            ans[i] = chr(((ord(ans[i])- 97 + array[i]) % 26)+97)
        
        return "".join(ans)
            