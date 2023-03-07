class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i<=k:
                count += min(tickets[k],tickets[i])
            else:
                count += min(tickets[i],tickets[k]-1)
        return count 
            