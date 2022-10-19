class Solution {
public:
   static bool comp(string  & s1,string  & s2){
        if(s1.size()>s2.size())
            return true;
       if(s2.size()>s1.size())
           return false;
        return s1>s2;
    }
    string kthLargestNumber(vector<string>& nums, int k) {
        k--;
        sort(nums.begin(),nums.end(),comp);
        return nums[k];
    }
};
