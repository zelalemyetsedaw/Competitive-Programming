class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count=0;
        int n=nums.size();
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            {
                if(nums[i] == nums[j] && i<j)
                {
                    ++count;
                }
            }
        
        return count;
        
    }
};