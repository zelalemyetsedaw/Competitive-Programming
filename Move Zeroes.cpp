class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
       int left = 0;
        int right = 0;
        while(right<n)
        {
            if(nums[right] == 0)
                right++;
            else
            {
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                left++;
                right++;
            }
        }
        
        
        
    }
};
