class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minuntilnow = float("inf")
        answer = 0
        for i in prices:
            answer = max(answer,i-minuntilnow)
            minuntilnow = min(minuntilnow,i)
            
        return answer