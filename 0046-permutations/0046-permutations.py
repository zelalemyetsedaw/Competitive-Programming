class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def permutations(temp, answer):
            if len(temp) == len(nums):
                answer.append(temp[:])  # Append a copy of temp
                return
                
            for num in nums:
                if num not in temp:
                    permutations(temp + [num], answer)  # Use a list instead of a tuple
                    
        permutations([], answer)  # Start with an empty list
        return answer