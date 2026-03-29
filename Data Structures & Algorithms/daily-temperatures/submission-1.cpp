class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // Add the temperature's index to the stack
        // If the stack is not empty and the current temperature is greater than that of the index at the top of the stack,
        //      remove the element's index at the top of the stack and then the answer is the 
        //      difference between the current index value and the removed index

        int n = temperatures.size();
        vector<int> ans(n,0);
        stack<int> st;  // stores indices

        for(int i = 0; i<n; i++){
            while(!st.empty() && temperatures[i] > temperatures[st.top()]){
                int idx = st.top();
                st.pop();
                ans[idx] = i - idx;
            }
            st.push(i);
        }
        return ans;
    }
};
