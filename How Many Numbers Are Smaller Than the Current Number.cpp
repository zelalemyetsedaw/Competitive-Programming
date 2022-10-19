class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
           vector<int> counts(101);
        int n = nums.size();
     vector<int> output(n);
     for(int i=0;i<=100;i++)
     {
         counts[i] = 0;
     }
     for(int i=0;i<n;i++)
     {
        ++counts[nums[i]];
     }
     for(int i=1;i<101;i++)
     {
         counts[i] = counts[i] + counts[i-1];
     }
     for(int i=0;i<n;i++)
     {
         if(nums[i]!=0)
         {output[i] = counts[nums[i] - 1];}
         else
         {output[i] = 0;}
     }
     return output;
    
    }
};
