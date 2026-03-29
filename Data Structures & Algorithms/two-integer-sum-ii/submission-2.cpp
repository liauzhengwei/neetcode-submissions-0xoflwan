class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while(left < right){
            int sum = numbers[left] + numbers[right];

            if(sum == target){
                // Return 1 based indices
                return {left + 1, right + 1};
            }
            else if(sum < target){
                left++;     // Move left pointer to the right to increase the sum
            }
            else{
                right--;    // Move right pointer to the left to decrease the sum
            }
        }
        // Return an empty vector if no solution is found
        return {};
    }
};
