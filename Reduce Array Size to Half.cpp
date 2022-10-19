class Solution {
public:
    int minSetSize(vector<int>& arr) {
        map<int,int> m;
        int n = arr.size();
        for(int i=0;i<n;i++)
        {
            m[arr[i]]++;
        }
        multimap<int,int,greater<int>> mm;
        for(auto x: m)
        {
            mm.insert({x.second,x.first});
        }
        int sum = n;
        int count = 0;
        for(auto i : mm)
        {
            sum -= i.first;
            count++;
            if(sum<=n/2)
            {
                
                break;
            }
        }
        return count;
        
    }
};
