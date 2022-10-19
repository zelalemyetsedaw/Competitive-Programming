class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
      stack< int> s;
      int j=0;
      for( auto x : pushed)
      {
          s.push( x);
          
          while( s.size()>0 && s.top()==popped[j])
          {
              s.pop();
              j++;
          }
          
          
      }
        return s.empty();
        
    }
};
