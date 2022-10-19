class Solution {
public:
    int maxVowels(string s, int k) {
        set<char> vowel = {'a','e','i','o','u'};
        int start = 0;
        int maxsum = 0;
        int wsum= 0;
        int n = s.size();
        for(int i=0;i<n;i++)
        {
            
            if(s[i] == *vowel.find(s[i]))
            {
                wsum++;
                
            }
            
            if(i-start+1 == k)
            {
                cout << wsum << endl;
                maxsum = max(wsum,maxsum);
                if(s[start] ==*vowel.find(s[start]))
                {wsum--;}
                
                start++;
                
            }
        }
        return maxsum;
        
    }
};
