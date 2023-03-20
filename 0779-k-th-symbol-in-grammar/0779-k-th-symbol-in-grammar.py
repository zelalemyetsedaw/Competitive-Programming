class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            if k==1:
                return 0
            else:
                return 1
            
        half=2**(n-1)
        if k<=half:
            return self.kthGrammar(n-1,k)
        else:
            result=self.kthGrammar(n-1,k-half)
            if result==0:
                return 1
            else:
                return 0
       
