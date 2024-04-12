/**
 * LeetCode [22]: Generate Parentheses
 * 
 * Given 'n' pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * 
 * Approach:
 * 1. Initialize an empty vector 'parenthesis' to store the generated combinations.
 * 2. Implement a recursive function 'makeParenthesis' to generate combinations of parentheses.
 * 3. The function takes four parameters: 'n' (number of pairs), 'str' (current string), 'open' (count of open parentheses), and 'close' (count of close parentheses).
 * 4. If the count of close parentheses exceeds the count of open parentheses, return.
 * 5. If both counts are equal to 'n', add the generated combination to the 'parenthesis' vector.
 * 6. Recursively call the function to generate combinations with an additional open parenthesis if the count of open parentheses is less than 'n'.
 * 7. Recursively call the function to generate combinations with an additional close parenthesis if the count of close parentheses is less than 'n'.
 * 8. Return the 'parenthesis' vector containing all generated combinations.
 */

class Solution {
public:
    vector<string> parenthesis;    

    vector<string> generateParenthesis(int n) {
        // Initialize an empty vector to store the generated combinations
        makeParenthesis(n, "", 0, 0);
        return parenthesis;
    }

    void makeParenthesis(int n, string str, int open, int close) {
        // If the count of close parentheses exceeds the count of open parentheses, return
        if (close > open)
            return;

        // If both counts are equal to 'n', add the generated combination to the 'parenthesis' vector
        if (close == n && open == n) {
            parenthesis.push_back(str);
            return;
        }

        // Recursively call the function to generate combinations with an additional open parenthesis if the count of open parentheses is less than 'n'
        if (open < n)
            makeParenthesis(n, str + "(", open + 1, close);

        // Recursively call the function to generate combinations with an additional close parenthesis if the count of close parentheses is less than 'n'
        if (close < n)
            makeParenthesis(n, str + ")", open, close + 1);
    }
};
