class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def findprimefactors(n,factorization):
            
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)

            return factorization
        answer = set()
        for i in nums:
            answer = findprimefactors(i,answer)
            
        return len(answer)

    