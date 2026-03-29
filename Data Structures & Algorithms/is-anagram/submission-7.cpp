#include <unordered_map>
#include <string>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the lengths are different, they cannot be anagrams
        if (s.length() != t.length()){
            return false;
        }

        // Create unordered maps for both strings
        std::unordered_map <char, int> count;

        // Count characters in the first string
        for (char c: s){
            count[c]++;
        }

        // Decrease count for characters in the second string
        for (char c: t){
            count[c]--;
        }

        // If all counts are 0, they are anagrams
        for(auto& entry: count){
            if(entry.second != 0){
                return false;
            }
        }
        return true;
    }
};
