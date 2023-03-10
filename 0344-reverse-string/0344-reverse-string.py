class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        
        def reverse(start,end):
            if start >= end:
                return 
            reverse(start+1,end-1)
            
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            
            
            
            
        reverse(0,len(s)-1)
            
            
       
    
        
        
        
        
        