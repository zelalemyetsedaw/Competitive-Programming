class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        d = defaultdict(int)
        for i in range(len(arr2)):
            d[arr2[i]] = i
        
        for j in range(len(arr1)):
            for i in range(1,len(arr1)):
                if arr1[i] in d and arr1[i-1] in d:
                    if d[arr1[i]] < d[arr1[i-1]]:
                        arr1[i],arr1[i-1] = arr1[i-1],arr1[i]
                elif arr1[i] in d and arr1[i-1] not in d:
                    arr1[i],arr1[i-1] = arr1[i-1],arr1[i]
                elif arr1[i] not in d and arr1[i-1] not in d:
                    if arr1[i] < arr1[i-1]:
                        arr1[i],arr1[i-1] = arr1[i-1],arr1[i]
                        
        return arr1
            