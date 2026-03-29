#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c:s){
            // Push opening brackets
            if(c == '(' || c == '{' || c == '['){
                st.push(c);
            }

            // Handle closing brackets
            else{
                if(st.empty()) return false;

                char top = st.top();
                st.pop();

                if((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')){
                    return false;
                }
            }
        }

        // Stack must be empty
        return st.empty();
    }
};
