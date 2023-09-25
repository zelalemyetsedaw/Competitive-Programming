class Solution:
    def minSteps(self, n: int) -> int:
        
        def recursion(copy_length,word_length,n):
            if word_length == n:
                return 0
            
            copy = float("inf")
            paste = float("inf")
            
            if copy_length != word_length:
                copy = 1 + recursion(word_length,word_length,n)
            if copy_length != 0 and word_length + copy_length <= n:
                paste = 1 + recursion(copy_length,word_length+copy_length,n)
                
            return min(copy,paste)
        
        return recursion(0,1,n)
        