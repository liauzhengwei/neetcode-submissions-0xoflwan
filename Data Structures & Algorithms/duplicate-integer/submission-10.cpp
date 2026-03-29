// for small arrays or memory concern
#include <vector>
#include <algorithm>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());    // Sort the array
        for (size_t i = 1; i < nums.size(); ++i){
            if(nums[i] == nums[i-1]){
                return true;    // Duplicate found
            }
        }
        return false;
    }
    // size_t is used to represent the size of any object in memory, used with `malloc`, `sizeof` and `strlen`
};