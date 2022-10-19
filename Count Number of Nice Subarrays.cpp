class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]%2==0)
            {
                nums[i] = 0;
            }
            else
            {
                nums[i] = 1;
            }
        }
        int n = nums.size();
        int sum = 0;
        map<int,int> m;
        m.insert({0,1});
        int count =0;
        for(int i=0;i<n;i++)
        {
            sum+=nums[i];
            
            auto it = m.find(sum-k);
            if(m.end()!= it)
            {
                count += it->second;
                
            }
            m[sum]++;
            
        }
        
        return count;
        
    }
};
