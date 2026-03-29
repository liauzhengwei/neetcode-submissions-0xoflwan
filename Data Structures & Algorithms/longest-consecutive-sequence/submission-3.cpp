#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Create an unordered set to store unique elements
        unordered_set<int> numSet(nums.begin(), nums.end());

        int longestStreak = 0;

        // Iterate through each number in the set
        for (int num: numSet){
            // Check if num is the start of a new sequence
            if(numSet.find(num - 1) == numSet.end()){ //'num - 1' not in the sequence
                int currentNum = num;
                int currentStreak = 1;

                // Count the length of the current sequence
                while(numSet.find(currentNum + 1) != numSet.end()){
                    currentNum++;
                    currentStreak++;
                }

                // Update the longest streak
                longestStreak = max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }
};
