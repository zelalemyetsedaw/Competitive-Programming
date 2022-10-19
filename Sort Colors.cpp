class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(3);
        vector<int> output(n);
        for(int i=0;i<3;i++)
            count[i] = 0;
        for(int i=0;i<n;i++)
            count[nums[i]]++;
        for(int i=1;i<3;i++)
            count[i]+=count[i-1];
        for(int i=0;i<n;i++)
            output[--count[nums[i]]] = nums[i];
        for(int i=0;i<n;i++)
            nums[i] = output[i];
        
    }
};
