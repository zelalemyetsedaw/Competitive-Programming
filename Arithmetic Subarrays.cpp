class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<int> temp;
        vector<bool> ans;
        for(int k=0;k<l.size();k++)
        {
          for(int i = l[k];i<=r[k];i++)
          {
              temp.push_back(nums[i]);
          }
            sort(temp.begin(),temp.end());
            bool t;
            int d = temp[1] - temp[0];
            for(int i=1;i<temp.size();i++)
            {
               
                if((temp[i]-temp[i-1]) == d)
                {
                    
                     t = true;
                }
                else
                {
                    t = false;
                    break;
                }
                
            }
            ans.push_back(t);
            temp.clear();
     }
        return ans;
    }
};
