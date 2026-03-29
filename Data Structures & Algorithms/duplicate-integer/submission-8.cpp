#include <iostream>
#include <map>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> freq;
        for (int num: nums){
            freq[num]++;
            if(freq[num] > 1){
                return true;    // Duplicate found
            }
        }
        return false;
    }
};