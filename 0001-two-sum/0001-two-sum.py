class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        nums.sort()
        i = 0
        j = len(nums)-1
        
        flag = True
        summ = 0
        while flag:
            summ = nums[i] + nums[j]
            if summ == target:
                flag = False
            if summ > target:
                j -= 1
            elif summ < target:
                i += 1
        if nums[i] == nums[j]:
            return [d[nums[i]][0],d[nums[j]][1]]
        return [d[nums[i]][0],d[nums[j]][0]]
                
        