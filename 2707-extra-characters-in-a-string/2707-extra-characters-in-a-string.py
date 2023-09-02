class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n, dictionary = len(s), set(dictionary)
        memo = {}
        
        def dp(start):
            if start == n:
                return 0
            if start in memo:
                return memo[start]

            
            ans = 1 + dp(start + 1)

           
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary:
                    ans = min(ans, dp(end + 1))
            memo[start] = ans
            return ans

        return dp(0)
                