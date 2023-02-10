class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> answer;
        for(int i=0;i<s.size();i++)
        {
            if((s[i]>=97 && s[i]<=122) || (s[i] >= 48 && s[i] <= 57))
            {
                answer.push_back(s[i]);
            }
            else if(s[i]>=65 && s[i]<=90)
            {
                answer.push_back(tolower(s[i]));
            }
            
        }
        vector<char> answer2 = answer;
        reverse(answer.begin(),answer.end()); 
        if(answer == answer2)
            return true;
        else
            return false;
        
    }
};