#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;

        int currArea = 0;
        int maxArea = 0;

        while (left < right){
            if(heights[left] < heights[right]){
                currArea = heights[left] * (right - left);
            }
            else{
                currArea = heights[right] * (right - left);
            }

            maxArea = max(maxArea, currArea);

            // Move the pointer pointing to the shorter line inward
            if(heights[left] < heights[right]){
                left++;
            } else{
                right--;
            }
        }
        return maxArea;
    }
};
