#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

// Comparator for the priority queue (min-heap) to sort by frequency
class Compare{
    public:
    // (number, count)
    // compare the count thats why .second
    bool operator()(const pair<int, int>& a, const pair<int, int>& b){
        return a.second > b.second; // Min heap: least frequent element comes out first
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Build the frequency map
        unordered_map<int, int> freq_map;
        for (int num: nums){
            freq_map[num]++;
        }

        // Use a priority queue to keep track of the top k frequent elements
        priority_queue< pair<int, int>, vector<pair<int, int>>, Compare> min_heap;

        // Iterate over the frequency map
        for (auto& entry: freq_map){
            min_heap.push(entry);   // Push the (number, frequency) pair into the heap

            // If the heap exceeds size k, remove the element with the smallest frequency
            if (min_heap.size() > k){
                min_heap.pop();
            }
        }

        // Extract the top k frequent elements from the heap
        vector<int> result;
        while(!min_heap.empty()){
            result.push_back(min_heap.top().first); // Get the number (not the frequency)
            min_heap.pop();
        }
        return result;
    }
};
