class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(),piles.end());
        int sum=0;
        int n= piles.size();
        int i=n-2;
        int j=0;
        while(j<n/3)
        {
            sum += piles[i];
            i-=2;
            j++;
        }
        return sum;
       
        
    }
};
