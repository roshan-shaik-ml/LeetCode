/**
 * LeetCode [20]: Valid Parentheses
 * 
 * Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * An input string is valid if:
 *   1. Open brackets must be closed by the same type of brackets.
 *   2. Open brackets must be closed in the correct order.
 * 
 * Approach:
 * 1. Use a stack to keep track of the opening brackets.
 * 2. Iterate through the string:
 *    - If the current character is a closing bracket and matches the top of the stack, pop the stack.
 *    - If the current character is an opening bracket, push it onto the stack.
 *    - If the current character is a closing bracket and doesn't match the top of the stack, return false.
 * 3. After iterating through the string, if the stack is empty, return true. Otherwise, return false.
 */

class Solution {
public:
    bool isValid(string s) {
        // Initialize a stack to keep track of opening brackets
        stack<char> stack;

        // Iterate through the string
        for(auto chr: s) {
            // If the current character is a closing bracket and matches the top of the stack, pop the stack
            if(chr == ')' && !stack.empty() && stack.top() == '(')
                stack.pop();
            else if(chr == ']' && !stack.empty() && stack.top() == '[')
                stack.pop();
            else if(chr == '}' && !stack.empty() && stack.top() == '{')
                stack.pop();
            // If the current character is an opening bracket, push it onto the stack
            else
                stack.push(chr);
        }

        // After iterating through the string, if the stack is empty, return true; otherwise, return false
        return stack.empty();
    }
};
