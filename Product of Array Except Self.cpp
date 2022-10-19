class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
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
