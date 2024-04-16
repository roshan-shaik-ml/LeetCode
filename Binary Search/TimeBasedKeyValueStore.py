"""
LeetCode [981]: Time Based Key-Value Store

Create a time-based key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp):
   Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp):
   Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
   If there are multiple such values, it returns the one with the largest timestamp_prev.
   If there are no values, it returns the empty string ("").

Example:
Input: 
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output: 
[null, null, "bar", "bar", null, "bar2", "bar2"]

Approach:
- We can use a dictionary to store key-value pairs where each key has a list of tuples (timestamp, value).
- For the `set` operation, we append the tuple (timestamp, value) to the list corresponding to the key.
- For the `get` operation, we perform binary search on the list corresponding to the key to find the value with the largest timestamp less than or equal to the given timestamp.

Code with Comments:
"""

from typing import List, Tuple

class TimeMap:

    def __init__(self):
        """
        Initialize the TimeMap class with an empty dictionary to store key-value pairs.
        """
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key and value, along with the given timestamp.

        Args:
        key: A string representing the key.
        value: A string representing the value.
        timestamp: An integer representing the timestamp.

        Returns:
        None
        """
        # If the key does not exist in the timemap, create a new entry with the key and a list containing the tuple (timestamp, value)
        if self.timemap.get(key) is None:
            self.timemap[key] = [(timestamp, value)]
        else:
            # If the key already exists, append the tuple (timestamp, value) to the list
            self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
        If there are multiple such values, it returns the one with the largest timestamp_prev.
        If there are no values, it returns the empty string ("").

        Args:
        key: A string representing the key.
        timestamp: An integer representing the timestamp.

        Returns:
        A string representing the value corresponding to the key and the largest timestamp less than or equal to the given timestamp.
        """
        # If the key does not exist in the timemap, return an empty string
        if self.timemap.get(key) is None:
            return ""
        else:
            # Perform binary search on the list corresponding to the key to find the value with the largest timestamp less than or equal to the given timestamp
            result = self.binarysearch(self.timemap[key], timestamp)
            return result

    def binarysearch(self, values: List[Tuple[int, str]], timestamp: int) -> str:
        """
        Perform binary search on a list of tuples to find the value with the largest timestamp less than or equal to the given timestamp.

        Args:
        values: A list of tuples representing (timestamp, value).
        timestamp: An integer representing the timestamp.

        Returns:
        A string representing the value with the largest timestamp less than or equal to the given timestamp.
        """
        # Initialize the result to an empty string
        res = ""
        left, right = 0, len(values) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                # If the timestamp at the mid position is less than or equal to the given timestamp,
                # update the result to the value at the mid position and move to the right half of the list
                left = mid + 1
                res = values[mid][1]
            else:
                # If the timestamp at the mid position is greater than the given timestamp,
                # move to the left half of the list
                right = mid - 1

        # Return the result
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
