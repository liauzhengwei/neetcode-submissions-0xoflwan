#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();

        // Sort the array to make it easier to avoid duplicates and use two pointer technique
        sort(nums.begin(), nums.end());

        // Loop through the array and find triplets
        for (int i=0; i<n-2; i++){  // Fix i for this iteration so that two pointer technique can be performed, repeat for all i until n-2
            // i < n-2 as left = i+1 and right = n-1, two pointer technique always performed on elements after the chosen i

            // Skip duplicate elements for the 'i' position
            if(i>0 && nums[i] == nums[i-1]) continue;

            int left = i+1;
            int right = n-1;

            // Use two pointer technique to find pairs that sum up to -nums[i]
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];

                if(sum == 0){
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for the `left` and `right` pointers
                    while(left < right && nums[left] == nums[left+1]) ++left;
                    while(left < right && nums[right] == nums[right-1]) --right;

                    // Move both pointers
                    ++left;
                    --right;
                } else if (sum < 0){
                    ++left;     // need a larger sum, move left pointer right
                } else{
                    --right;    // need a smaller sum, move right pointer left
                }
            }
        }
        return result;
    }
};
