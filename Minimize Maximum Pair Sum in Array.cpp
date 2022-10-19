class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int right = n-1;
        sort(nums.begin(),nums.end());
        int prev = 0;
        int sum = 0;
        while(left<right)
        {
             sum = nums[left] + nums[right];
            if(sum>prev)
            {
                prev = sum;
            }
            left++;
            right--;
            
        }
        return prev;
        
    }
};
