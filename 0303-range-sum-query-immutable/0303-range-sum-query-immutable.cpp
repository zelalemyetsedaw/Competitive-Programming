class NumArray {
public:
    vector<int> answer;
    NumArray(vector<int>& nums) {
        
        answer = nums;
        for(int i=1;i<nums.size();i++)
        {
            answer[i] += answer[i-1];
        }
        
    }
    
    int sumRange(int left, int right) {
        if(left != 0)
        {
            return answer[right] - answer[left-1];
        }
        else
            return answer[right];
        
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */