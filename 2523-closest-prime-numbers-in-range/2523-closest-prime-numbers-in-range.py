class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        #1 is prime
        primearr = [1] * (right+1)
        primearr[0] = 0
        primearr[1] = 0
        
        for i in range(2,floor(sqrt(right+1))+1):
            if primearr[i] == 1:
                j = 2
                while i*j < right+1:
                    primearr[i*j] = 0
                    j+=1
                
        primearray = []
        for i in range(right-left+1):
            if primearr[left] == 1:
                primearray.append(left)
            left += 1
           
            
        a , b = 0 , 10 ** 6
        
        for i in range(1,len(primearray)):
            if (primearray[i] - primearray[i-1]) < (b - a):
                a , b = primearray[i-1],primearray[i]
                if b-a <= 2:
                    break
            
        if a == 0:
            return [-1,-1]
        else:
            return [a,b]