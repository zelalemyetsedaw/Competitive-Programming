
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        stack<long long> s;
        for(string x: tokens)
        {
              if(x == "+")
                {
                    int a = s.top();
                s.pop();
                int y = s.top();
                s.pop();
                
                int result= a + y;
                  s.push(result);
                }
              else if(x == "-")
                {
                int a = s.top();
                s.pop();
                int y = s.top();
                s.pop();
                
                int result= y - a;
                  s.push(result);
                }
             else if(x == "*")
                {
                   long long a = s.top();
                s.pop();
                long long y = s.top();
                s.pop();
                
                long long result= a * y;
                 s.push(result);
                }
             else if(x == "/")
                {
                    int a = s.top();
                s.pop();
                int y = s.top();
                s.pop();
                
                int result= y / a;
                 s.push(result);
                }
            else
                s.push(stoi(x));
                
                
            }
        
        return s.top();
        
    }
};
