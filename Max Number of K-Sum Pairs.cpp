class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        
        int n= nums.size();
        sort(nums.begin(),nums.end());
        int left = 0;
        int right = n-1;
        int ans =0;
        while(left<right)
        {
            if((nums[left] + nums[right]) == k)
            {
                left++;
                right--;
                ans++;
            }
            else if(nums[left]+nums[right]>k)
            {
                right--;
            }
            else
            {
                left++;
            }
        }
        return ans;
        
    }
};
