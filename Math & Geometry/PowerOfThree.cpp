/*
LeetCode [326]: Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Approach:
1. Check if the given number is less than or equal to 0. If so, return false.
2. Divide the number by 3 repeatedly until it is no longer divisible by 3.
3. If the resulting number is 1, return true; otherwise, return false.

Code with Comments:
*/

class Solution {
public:
    bool isPowerOfThree(int n) {
        // Check if n is less than or equal to 0
        if (n <= 0)
            return false;
        
        // Divide n by 3 repeatedly until it's not divisible by 3
        while (n % 3 == 0) {
            n /= 3;
        }

        // If n is 1, it's a power of three
        if (n == 1)
            return true;
        // Otherwise, it's not a power of three
        return false;
    }
};
