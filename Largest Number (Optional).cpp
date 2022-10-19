class Solution {
public:
   
    string largestNumber(vector<int>& nums) {
      int n = nums.size();
        vector<string> s(n) ;
        
        for(int i=0;i<n;i++)
        {
            s[i] += to_string(nums[i]);
        }
        for(int i=0;i<s.size()-1;i++)
            for(int j=i+1;j<s.size();j++)
            {
                if(s[j]+s[i] > s[i] + s[i])
                {
                    string temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        string answer;
        for(int i=0;i<n;i++)
            answer += s[i];
        if(s[0]=="0")
            answer = "0";
        
        return answer;
        
    }
};
