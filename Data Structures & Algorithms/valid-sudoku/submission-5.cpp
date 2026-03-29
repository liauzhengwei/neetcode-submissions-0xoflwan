#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Create sets for rows, columns, and 3x3 subgrids
        vector<unordered_set<char>> rows(9), cols(9), subgrids(9);

        // Iterate through each cell in the board
        for (int i = 0; i < 9; ++i){
            for(int j = 0; j < 9; ++j){
                char num = board[i][j];
                if (num == '.') continue;   // Skip empty cells

                // Calculate the index for the 3x3 subgrid (0 to 8), the smaller boxes
                int subgridIndex = (i / 3) * 3 + j / 3;

                // Check if the number already exists in the current row, column or subgrid
                if (rows[i].count(num) || cols[j].count(num) || subgrids[subgridIndex].count(num)){
                    return false;   // Invalid if any repetition is found, when the `.count()` is 1
                }

                // Add the number to the corresponding row, column, and subgrid
                rows[i].insert(num);
                cols[j].insert(num);
                subgrids[subgridIndex].insert(num);

            }
        }
        return true;    // No repetition found
    }
};
