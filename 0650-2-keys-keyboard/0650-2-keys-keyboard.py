class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = defaultdict(int)
        def recursion(copy_length,word_length,n):
            if memo[(copy_length,word_length)]:
                return memo[(copy_length,word_length)]
            if copy_length == word_length and copy_length + word_length > n:
                return float("inf")
            if word_length == n:
                return 0
            
            copy = float("inf")
            paste = float("inf")
            
            if copy_length != word_length:
                copy = 1 + recursion(word_length,word_length,n)
            if copy_length != 0 and word_length + copy_length <= n:
                paste = 1 + recursion(copy_length,word_length+copy_length,n)
                
            memo[(copy_length,word_length)] = min(copy,paste)
            return memo[(copy_length,word_length)]
        
        return recursion(0,1,n)
        