class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // piles[i]: number of bananas in ith pile
        // banana eating rate/hr: k
        // if pile < k: all bananas eaten
        // FIND: MIN int k to eat all bananas in h hours

        // piles[i] / k < h
        int end = *max_element(piles.begin(), piles.end()); // gets the largest banana pile
        int start = 1;

        while(start <= end){
            long long hours = 0;
            int mid = start + (end - start) / 2;

            for(int pile: piles){
                hours += (pile + mid - 1) / mid;  // ceiling division due to '+ mid - 1'
            }

            if (hours <= h){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        return start;
    }
};
