class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int wsum = 0;
        int start = 0;
        int zerosum = 0;
        int maxsum = 0;
        for(int i=0;i<n;i++)
        {
            wsum = i-start+1;
            if(nums[i] == 0)
            {
                zerosum++;
            }
            if(i==n-1 && zerosum <=1)
            {
                maxsum = max(wsum-1,maxsum);
            }
            if(zerosum>1)
            {
                maxsum = max(wsum-2,maxsum);
                while(nums[start]!=0)
                    start++;
                start++;
                zerosum--;
                
                
            }
        }
        return maxsum;
        
    }
};
