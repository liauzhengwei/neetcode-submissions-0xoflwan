class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find the pivot then search from there
        int left = 0;
        int right = nums.size()-1;

        while (left <= right){
            int mid = left + (right - left) /2;

            if (nums[mid] == target){
                return mid;
            }

            // Left half is sorted
            if(nums[left] <= nums[mid]){
                // Located in the left half
                if(nums[left] <= target && target < nums[mid]){
                    right = mid - 1;
                } else{ // Located in the right half
                    left = mid + 1;
                }
            }
            // Right half is sorted
            else{
                // Located in the left half
                if(nums[mid] < target && target <= nums[right]){
                    left = mid + 1;
                }
                else{ // Located in the right half
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};
