class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty()) return 0;

        int left = 0;
        int right = height.size() - 1;
        int leftMax = 0; // maximum height seen from the left
        int rightMax = 0; // maximum height seen from the right
        int result = 0; // accumulating the total trapped water

        while (left < right){
            if(height[left] < height[right]){
                // Move the left pointer
                if(height[left] >= leftMax){
                    leftMax = height[left]; // Update leftMax if the current height is greater than the previous one
                } else{
                    result += leftMax - height[left];
                }
                left++;
            } else{
                // Move the right pointer
                if(height[right] >= rightMax){
                    rightMax = height[right];
                } else{
                    result += rightMax - height[right];
                }
                right--;
            }
        }
        return result;
    }
};
