class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        int n=changed.size();
        if(n%2 !=0) return {};
        map<int,int> m;
        for(int i=0;i<n;i++)
            m[changed[i]]++;
        sort(changed.begin(),changed.end());
        vector<int> answer;
        for(int i=0;i<n;i++)
        {
            int freq1 = m[changed[i]];
            int freq2 = m[changed[i]*2];
            if(freq1>0 && freq2>0)
            {answer.push_back(changed[i]);
             m[changed[i]]--;
             m[changed[i]*2]--;
            }
            
            else if(freq1>0 && freq2 == 0)
                return {};
            
        }
        return answer;
        
    }
};
