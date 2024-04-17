"""
LeetCode [150]: Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Approach:
- Use a stack to keep track of operands.
- Iterate through each token in the input list.
- If the token is an operand, push it onto the stack.
- If the token is an operator, pop two operands from the stack, perform the operation, and push the result back onto the stack.
- Finally, the result will be the only element left in the stack.

"""

from typing import List
import collections

class Solution:   

    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack to store operands
        stack = collections.deque()
        # Define operators set
        operators = set('+*/-')
        
        # Iterate through each token in the input list
        for token in tokens:
            # If the token is not an operator, push it onto the stack
            if not token in operators:
                stack.append(int(token))
            else:
                # If the token is an operator, pop two operands from the stack
                b, a = stack.pop(), stack.pop()
                # Perform the operation based on the operator
                if token == '+':
                    stack.append((a + b))
                elif token == '-':
                    stack.append((a - b))
                elif token == '*':
                    stack.append((a * b))
                elif token == '/':
                    # In Python, integer division is performed using //
                    stack.append((int(a / b)))
        
        # The result will be the only element left in the stack
        return stack[0]
