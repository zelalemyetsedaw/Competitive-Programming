class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def combination(index,arr,temp,n,answer):
            if index == n :
                if len(temp)>=2 and (not answer or  tuple(temp) not in answer):
                    answer.add(tuple(temp.copy()))
                return answer

            if not temp or temp[-1] <= arr[index]:
                temp.append(arr[index])
                answer = combination(index+1,arr,temp,n,answer)

                temp.pop()
            answer = combination(index+1,arr,temp,n,answer)
            return answer

        
        temp = []
        n = len(nums)
        answer = set()

        return list(combination(0,nums,temp,n,answer))

        
            