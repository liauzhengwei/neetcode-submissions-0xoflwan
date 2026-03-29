#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        /*
        std::unordered_set<int>seen;

        // unordered_set.find takes the value being searched
        // if num in the set, it returns an iterator pointing to the element in the set
        // if num is not in the set, it returns unordered_set.end(), a special iterator that indicates the end of the set
        for (int num : nums){
            // If the number is already in the set, it is a duplicate
            if (seen.find(num) != seen.end()){
                return true;
            }
            seen.insert(num);
        }
        return false;
        */

        std::sort(nums.begin(), nums.end());    // Sort the array
        for (size_t i = 1; i < nums.size(); ++i){
            if(nums[i] == nums[i-1]){
                return true;    // Duplicate found
            }
        }
        return false;



    }
    // std::set sorts the elements and has higher memory overhead
};