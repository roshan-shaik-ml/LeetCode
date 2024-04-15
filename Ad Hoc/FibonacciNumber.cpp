/*
LeetCode [509]: Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is, F(0) = 0, F(1) = 1, and F(n) = F(n - 1) + F(n - 2) for n > 1.

Approach:
1. Recursively calculate the Fibonacci number for the given index.
2. Base case: If the index is 0 or 1, return the index itself.
3. Otherwise, return the sum of the Fibonacci numbers for (n-1)th and (n-2)th indices.

Code with Comments:
*/

class Solution {
public:
    int fib(int n) {
        // Base case: If n is 0 or 1, return n
        if (n == 0 || n == 1)
            return n;

        // Recursively calculate Fibonacci number for (n-1)th and (n-2)th indices
        return fib(n - 1) + fib(n - 2);
    }
};
