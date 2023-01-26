class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = [0 for x in range(len(arr))]
        new[len(arr)-1] = -1
        for i in range(len(arr)-2,-1,-1):
            new[i] = max(arr[i+1],new[i+1])
        return new