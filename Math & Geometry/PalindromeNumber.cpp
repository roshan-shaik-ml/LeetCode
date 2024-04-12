/**
 * LeetCode [9]: Palindrome Number
 * 
 * Determine whether an integer is a palindrome.
 * An integer is a palindrome when it reads the same backward as forward.
 * 
 * Approach:
 * 1. Check if the input number is negative, as negative numbers can't be palindromes.
 * 2. Get the reverse of the input number.
 * 3. Compare the reverse with the original number. If they are equal, the number is a palindrome.
 */

class Solution {
public:
    bool isPalindrome(int x) {
        // Check if the number is negative, as negative numbers can't be palindromes
        if(x < 0)
            return false;

        // Get the reverse of the input number
        long long reverse = getReverse(x);
        
        // Compare the reverse with the original number
        if(reverse == x)
            return true;
        else
            return false;
    }

    // Function to get the reverse of a number
    long long getReverse(long long x) {
        long long reverse = 0;
        while(x > 0) {
            reverse = reverse * 10;
            reverse += x % 10;
            x = x / 10;
        }
        return reverse;
    }
};
