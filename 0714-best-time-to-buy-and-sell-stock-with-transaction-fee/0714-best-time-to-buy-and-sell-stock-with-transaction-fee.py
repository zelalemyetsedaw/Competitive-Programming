class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pos=-prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            pos=max(pos,profit-prices[i])
            profit=max(profit,pos+prices[i]-fee)

        return profit 