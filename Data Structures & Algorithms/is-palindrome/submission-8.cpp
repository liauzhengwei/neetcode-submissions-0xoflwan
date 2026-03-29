#include <string>
#include <cctype>   // for tolower() function
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        // Converts the string to lowercase and remove spaces
        string cleanedStr = "";
        for(char ch: s){
            if(isalnum(ch)){   // Skip spaces
                cleanedStr += tolower(ch);  // Convert to lowercase and add to cleanedStr
            }
        }

        // Check if cleanedStr is a palindrome
        int start = 0;
        int end = cleanedStr.length() - 1;

        while (start < end){
            if (cleanedStr[start] != cleanedStr[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
