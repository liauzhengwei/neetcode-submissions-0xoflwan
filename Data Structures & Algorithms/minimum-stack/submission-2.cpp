#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> st;
    stack<int> minSt;

public:
    MinStack() {
    }
    
    // Create a minimum stack and manipulate the stack so that it stores the minimum value at all times
    void push(int val) {
        st.push(val);
        if(minSt.empty() || val <= minSt.top()){
            minSt.push(val);
        }
    }
    
    void pop() {
        if(st.top() == minSt.top()){
            minSt.pop();
        }
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};
