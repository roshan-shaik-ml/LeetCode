/*
LeetCode [412]: Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Approach:
1. Iterate from 1 to n.
2. Check if the current number is divisible by both 3 and 5, if so, append "FizzBuzz" to the result.
3. Check if the current number is divisible by 3, if so, append "Fizz" to the result.
4. Check if the current number is divisible by 5, if so, append "Buzz" to the result.
5. Otherwise, append the number itself as a string to the result.

Code with Comments:
*/

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> fizzBuzz(int n) {
        std::vector<std::string> arr;

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0)
                arr.push_back("FizzBuzz");
            else if (i % 3 == 0)
                arr.push_back("Fizz");
            else if (i % 5 == 0)
                arr.push_back("Buzz");
            else
                arr.push_back(std::to_string(i));
        } 

        return arr;  
    }
};
