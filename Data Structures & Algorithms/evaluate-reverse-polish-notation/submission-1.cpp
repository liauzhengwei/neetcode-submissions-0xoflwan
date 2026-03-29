#include <vector>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // Every time an operation is encountered, remove two elements and then perform the operation
        stack<int> st;

        for(string token: tokens){
            // If operator
            if(token == "+" || token == "-" ||
                token == "*" || token == "/"){
                    int b = st.top(); st.pop();
                    int a = st.top(); st.pop();

                    if(token == "+") st.push(a + b);
                    else if(token == "-") st.push(a - b);
                    else if(token == "*") st.push(a * b);
                    else st.push(a / b);    // truncates towards zero
            }
            // If number
            else{
                st.push(stoi(token));   // Remember to convert string to integer
            }
        }
        return st.top();
    }
};
