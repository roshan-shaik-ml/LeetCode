/**
 * LeetCode [155]: Min Stack
 * 
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * 
 * Approach:
 * 1. Use a stack to store pairs of integers (value, minimum) where minimum represents the minimum value seen so far.
 * 2. When pushing a new value onto the stack, compare it with the current minimum and update accordingly.
 * 3. Each element in the stack will contain its corresponding minimum value.
 * 
 * Code with Comments:
 */

#include <stack>
#include <utility>

class MinStack {
public:
    std::stack<std::pair<int, int>> stck;  // Stack to store pairs (value, minimum)

    MinStack() {
        // Constructor
    }
    
    void push(int val) {
        // Push a new value onto the stack
        if (stck.empty())
            stck.push({val, val});
        else {
            int current_min = stck.top().second;
            if (val < current_min)
                stck.push({val, val});  // Update minimum if necessary
            else
                stck.push({val, current_min});
        }
    }
    
    void pop() {
        // Remove the top element from the stack
        stck.pop();
    }
    
    int top() {
        // Get the value of the top element
        return stck.top().first;
    }
    
    int getMin() {
        // Retrieve the minimum value in the stack
        return stck.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
