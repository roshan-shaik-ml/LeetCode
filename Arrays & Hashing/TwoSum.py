class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the frequency of each number along with its index
        freq = {}
        for idx in range(0, len(nums)):
            freq[nums[idx]] = idx

        # Iterate through the list of numbers
        for idx in range(0, len(nums)):
            # Calculate the complement needed to reach the target
            find = target - nums[idx] 
            # Check if the complement exists in the dictionary and it's not the same index as the current number
            if(freq.get(find) == None or freq.get(find) == idx):
                # If not found or it's the same index, continue to the next iteration
                continue
            else:
                # If found, return the indices of the two numbers that add up to the target
                return [idx, freq.get(find)]
