class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = defaultdict(int)
        def recursion(left,right):
            if (left,right) in memo:
                return memo[(left,right)]
            if left == right:
                return 1
            if left > right:
                return 0
            
            if s[left] == s[right]:
                memo[(left,right)] = 2 + recursion(left+1,right-1) 
            else:
                memo[(left,right)] = max(recursion(left+1,right),recursion(left,right-1))
            
            return memo[(left,right)]
        
        return recursion(0,len(s)-1)