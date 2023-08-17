class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefixsum = [0] * (len(s) + 1)
        
        for start,end,direction in shifts:
            if direction == 0:
                prefixsum[start] += -1
                prefixsum[end+1] += 1
            else:
                prefixsum[start] += 1
                prefixsum[end+1] += -1
                
            
        for i in range(1,len(s)+1):
            prefixsum[i] += prefixsum[i-1]
        
        
        answer = ""
        for i in range(len(s)):
            answer += chr((((ord(s[i]) + prefixsum[i])-97) %26) + 97)
        
        return answer
        
        