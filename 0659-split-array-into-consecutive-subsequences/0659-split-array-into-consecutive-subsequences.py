class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        listLengthThatEndWith = defaultdict(list)
    
        for n in nums:
            
            end = n - 1
            
            if listLengthThatEndWith[end]:
                 heappush(listLengthThatEndWith[n], heappop(listLengthThatEndWith[end]) + 1)
                
            else:
                heappush(listLengthThatEndWith[n], 1)
                
        for value in listLengthThatEndWith.values():
            if value and value[0]<3 :
                return False
                
        return True
            