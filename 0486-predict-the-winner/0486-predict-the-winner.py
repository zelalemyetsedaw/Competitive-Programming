class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(left,right,score1,score2,turn):
            if left > right:
                return score1 >= score2
            if turn == 1:
                leftway = helper(left+1,right,score1+nums[left],score2,0)
                rightway = helper(left,right-1,score1 + nums[right],score2,0)
                
                return leftway or rightway
            else:
                leftway = helper(left+1,right,score1,score2 + nums[left],1)
                rightway = helper(left,right-1,score1,score2 + nums[right],1)
                
                return leftway and rightway
            
        return helper(0,len(nums)-1,0,0,1)