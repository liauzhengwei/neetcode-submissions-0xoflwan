class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        
        int row = matrix.size();
        int col = matrix[0].size();

        int start = 0;
        int end = row - 1;

        while (start <= end){
            int mid = start + (end - start) / 2;

            if (matrix[mid][0] <= target && target <= matrix[mid][col-1]){
                int st = 0;
                int en = col - 1;

                while(st <= en){
                    int mi = st + (en - st) /2;
                    if(matrix[mid][mi] == target){
                        return true;
                    }
                    else if(matrix[mid][mi] < target){
                        st = mi + 1;
                    }
                    else if(matrix[mid][mi] > target){
                        en = mi - 1;
                    }
                }
                return false;
            }

            else if(matrix[mid][0] > target){
                end = mid - 1;
            }
            else if(matrix[mid][col-1] < target){
                start = mid + 1;
            }
        }
        return false;
    }
};
