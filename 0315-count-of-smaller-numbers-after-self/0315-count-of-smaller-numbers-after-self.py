class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def mergeSort(l,r):
            if l>=r:
                return 
            mid=(l+r)//2
            mergeSort(l,mid)
            mergeSort(mid+1,r)
            sortList=[]
            i,j=mid,r
            while i>=l and j>=mid+1:
                if arr[i][1]>arr[j][1]:
                    ans[arr[i][0]]+=j-mid
                    sortList.append(arr[i])
                    i-=1
                else:
                    sortList.append(arr[j])
                    j-=1
            if i>=l:
                sortList+=arr[l:i+1][::-1]
            else:
                sortList+=arr[mid+1:j+1][::-1]
            arr[l:r+1]=sortList[::-1]
            
        n=len(nums)
        arr=list(enumerate(nums))
        ans=[0]*n
        mergeSort(0,n-1)
        return ans
            