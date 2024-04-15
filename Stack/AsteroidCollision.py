"""
LeetCode [735]: Asteroid Collision

Given a list of asteroids moving in the same direction, returns the final state of the asteroids
after all collisions.

Approach:
1. Iterate through the list of asteroids and simulate the collisions using a stack. 
2. When encountering a new asteroid, check if it collides with the asteroids in the stack. 
3. Handle collisions according to the given rules.

Code with Comments:
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Given a list of asteroids moving in the same direction, returns the final state of the asteroids
        after all collisions.

        Args:
        - asteroids: A list of integers representing the sizes of the asteroids, where negative integers
          represent asteroids moving to the left and positive integers represent asteroids moving to the right.

        Returns:
        - stack: A list representing the final state of the asteroids after all collisions, with only the surviving asteroids.
        """
        # Initialize a stack to store the asteroids
        stack = [] 
        idx = 0
        
        # Iterate through each asteroid in the list
        while idx < len(asteroids):
            # Flag to track whether the current asteroid has been destroyed
            flag = 0
            
            # Check for collisions with the asteroids in the stack
            while stack and idx < len(asteroids) and asteroids[idx] ^ stack[-1] < 0:
                # Case 1: Big asteroid hits smaller asteroid, smaller asteroid is destroyed
                if stack[-1] > 0 and stack[-1] + asteroids[idx] < 0:
                    stack.pop()
                # Case 2: Equal-sized asteroids collide, both are destroyed
                elif stack[-1] > 0 and stack[-1] + asteroids[idx] == 0:
                    stack.pop()
                    flag = 1
                    break
                # Case 3: Big asteroid survives, smaller asteroid is destroyed
                elif stack[-1] > asteroids[idx]:
                    flag = 1
                    break
                else:
                    break
            
            # Add the current asteroid to the stack if it has not been destroyed
            if flag == 0 and idx < len(asteroids):
                stack.append(asteroids[idx])
            
            idx += 1
        
        return stack
