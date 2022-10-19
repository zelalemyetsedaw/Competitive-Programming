class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    map<char,int> v;
        
        int i=0;
        int j=0;
        int n = s.size();
        int maxsize = 0;
        int wsize = 0;
        while(j<n)
        {
            v[s[j]]++;
            
            if(v[s[j]]==2)
            {
                while(s[i]!=s[j])
                {
                    v[s[i]]--;
                    i++;
                }
                i++;
                v[s[j]]--;
            }
            
            wsize = j-i+1;
            maxsize = max(wsize,maxsize);
            j++;
            
        }
        
        return maxsize;
    }
};
