class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int start = 0;
        int wsum = 0;
        int count = 0;
        for(int i=0;i<n;i++)
        {
            wsum += arr[i];
            if(i-start+1 == k)
            {
                if(wsum/k >= threshold)
                    count++;
                
                wsum -= arr[start];
                start++;
            }
        }
        return count;
        
    }
};
