/**
 * Determines whether an integer is a palindrome.
 * @param {number} x - The integer to check.
 * @return {boolean} - True if the integer is a palindrome, false otherwise.
 */
var isPalindrome = function(x) {
    // Check if the number is negative, as negative numbers can't be palindromes
    if(x < 0)   
        return false;
    
    // Initialize variables to store the reversed number and a temporary copy of the original number
    let reversed = 0;
    let temp = x;

    // Reverse the number by extracting digits and building the reversed number
    while(x != 0) {
        reversed = reversed * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    
    // Check if the reversed number is equal to the original number
    return reversed == temp;
};
