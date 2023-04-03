class Solution:
    def maxLength(self, arr: List[str]) -> int:
        answer = 0
        temp  = set()
        def backtracking(index,temp,n,answer):
            if index == n:
                answer = max(answer,len(temp.copy()))
                return answer
            
            flag = False
            if len(set(arr[index])) == len(arr[index]):
                for i in arr[index]:
                    if i in temp:
                        flag = True
                        break
            else:
                flag = True
            
            if flag == False:
                for i in arr[index]:
                    temp.add(i)
                   
                answer = backtracking(index+1,temp,n,answer)
                
                for i in arr[index]:
                    temp.remove(i)
            answer = backtracking(index+1,temp,n,answer)
            return answer
        
        
        return backtracking(0,temp,len(arr),answer)
            