class Solution {
public:
    
    int maxSum(vector<vector<int>>& grid) {
        int rows = grid.size();
        int columns = grid[0].size();
        int max_sum = 0;
        
        for(int i=1;i<rows-1;i++)
        {
            for(int j=1;j<columns-1;j++)
            {
            int sum = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] +                         grid[i+1][j-1] + grid[i+1][j]+ grid[i+1][j+1];
                max_sum = max(max_sum,sum);
            }
        }
        
        return max_sum;
        
        
        
    }
};
