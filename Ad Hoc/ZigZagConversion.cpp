/*
LeetCode [6]: ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Approach:
1. Create a vector of strings to represent each row of the zigzag pattern.
2. Iterate through the input string and assign each character to the appropriate row based on the direction of traversal.
3. Concatenate the strings in the vector row by row to form the final zigzag pattern.

Code with Comments:
*/

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        // Return the input string if numRows is 1 or if the string length is less than numRows
        if (numRows == 1 || s.length() < numRows)
            return s;
        
        // Initialize variables to represent the direction of traversal and rows for the zigzag pattern
        bool goingDown = true; // true -> down, false -> up
        vector<string> v(numRows); // Vector to store strings representing each row
        int i = 0; // Current row index

        // Iterate through the input string
        for (auto ch : s) {
            v[i] += ch; // Append the current character to the string of the current row

            // Update the row index based on the direction of traversal
            if (goingDown == true)
                i += 1;
            else
                i -= 1;

            // Update the direction of traversal when reaching the first or last row
            if (i == numRows - 1)
                goingDown = false;
            else if (i == 0)
                goingDown = true;                       
        }
        
        // Concatenate the strings in the vector row by row to form the final zigzag pattern
        string ans = "";
        for (auto row : v) {
            ans += row;
        }
        return ans;
    }
};
