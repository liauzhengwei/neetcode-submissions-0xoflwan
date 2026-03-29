#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 1);   // Initialise the output array with 1s

        // First pass: calculate left products
        int leftProduct = 1;
        for (int i = 0; i < n; i++){
            output[i] = leftProduct;
            leftProduct *= nums[i]; // Update leftProduct for the next iteration
        }

        // Second pass: calculate right products
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--){
            output[i] *= rightProduct;
            rightProduct *= nums[i]; // Update rightProduct for the next iteration
        }
        return output;
    }
};
