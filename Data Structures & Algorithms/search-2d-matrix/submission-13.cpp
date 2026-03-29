class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;

        int row = matrix.size();
        int col = matrix[0].size();

        int left = 0;
        // Obtain the size of the 2D array
        int right = row * col -1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            
            // Treat the 2D array as a 1D array instead
            // By dividing by the number of columns, the row number can be obtained
            // By finding the remainder when divided by the column, the column number can be obtained
            int r = mid / col;  
            int c = mid % col;

            if(matrix[r][c] == target){
                return true;
            } else if (matrix[r][c] < target){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
};
