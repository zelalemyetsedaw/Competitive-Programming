class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        ind = 0
        while len(arr)>1:
            ind += k-1
            if(ind>=len(arr)):
                ind %= len(arr)
            arr.pop(ind)
        return arr[0]
                
            