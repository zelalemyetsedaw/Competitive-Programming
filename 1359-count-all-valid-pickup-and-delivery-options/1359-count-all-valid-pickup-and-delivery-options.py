class Solution:
    def countOrders(self, n: int) -> int:
        
        temp = temp2 = 1
        for i in range(1,n+1):
            temp = (temp * i) % (10 ** 9 + 7)
        
        x = 1
        
        for i in range(1,n+1):
            temp2 = (temp2 * x) % (10 ** 9 + 7)
            x += 2
            
        return (temp * temp2) % (10 ** 9 + 7)
            