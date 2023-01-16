class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        print(arr)
        j=0
        while(len(arr)!=1):
            j += k-1
            print(j)
            while(j>len(arr)-1):
                j = j % len(arr)
            arr.pop(j)
            print(arr)
            
            
        return arr[0]
            