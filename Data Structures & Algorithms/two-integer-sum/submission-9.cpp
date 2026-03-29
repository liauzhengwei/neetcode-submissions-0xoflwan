#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_map;    // Map to store its number and its index

        for (int i = 0; i < nums.size(); ++i){
            int complement = target - nums[i];

            // If the complement exists in the map, solution found
            if(num_map.find(complement) != num_map.end()){
                return {num_map[complement], i};    // Return the indices of the pair
            }

            // Otherwise, add the current number to the map with its index
            num_map[nums[i]] = i;
        }
        return {};  // No solution found
    }
};
