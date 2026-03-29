#include <algorithm>    // for sorting
#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramGroups;

        //Loop througn all the strings in the input list
        for (const string& str: strs){
            string sortedStr = str; // Copy the string to sort it
            sort(sortedStr.begin(), sortedStr.end());   // Sort the characters

            // Group the original string by the sorted version
            anagramGroups[sortedStr].push_back(str);
        }

        // Prepare the result as a vector of vectors
        vector<vector<string>> result;
        for (auto& entry: anagramGroups){
            result.push_back(entry.second); // Push the anagram group to the result
        }
        return result;
    }
    // vector<string> is an array of string
};
