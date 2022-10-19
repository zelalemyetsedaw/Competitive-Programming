class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> m;
        int n = nums.size();
        vector<int> answer;
        vector<int>ans;
        for(auto x:nums)
        {
            m[x]++;
        }
        multimap<int,int,greater<int>> mm;
        for(auto x: m)
        {
            mm.insert({x.second,x.first});
        }
        for(auto x: mm)
        {
            answer.push_back(x.second);
            
        }
        for(int i=0;i<k;i++)
        {
            ans.push_back(answer[i]);
        }
        return ans;
    }
};
