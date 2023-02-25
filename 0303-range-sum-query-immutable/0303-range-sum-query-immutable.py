class NumArray(object):

    def __init__(self, nums):
        self.answer = nums
        self.length = len(nums)
        for i in range(1,self.length):
            self.answer[i] += self.answer[i-1]

    def sumRange(self, left, right):
        if left!=0:
            return self.answer[right]-self.answer[left-1]
        else:
            return self.answer[right]
            
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)