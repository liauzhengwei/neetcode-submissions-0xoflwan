#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    // Encode a list of strings to a single string
    string encode(vector<string>& strs) {
        string encoded = "";
        for (const string& str : strs){
            encoded += to_string(str.size()) + "#" + str;   // format: "length#str"
        }
        return encoded;
    }

    // Decodes a single string to a list of strings
    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;

        while(i < s.size()){
            // Find the position of '#'
            int j = i;
            while (s[j] != '#') j++;    // Find the delimiter #

            // Extract the length of the string
            int length = stoi(s.substr(i, j - i));    // Convert substring to integer
            i = j + 1; // Move the pointer past the '#'

            // Extract the string using the length
            string str = s.substr(i, length);
            decoded.push_back(str);

            // Move the pointer past the decoded string
            i += length;
        }
        return decoded;
    }
};
