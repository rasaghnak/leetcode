class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the indices of elements we have seen
        num_to_index = {}
        
        # Iterate over the list with index and value
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # Return the indices of the complement and current number
                return [num_to_index[complement], i]
            
            # Store the index of the current number in the dictionary
            num_to_index[num] = i

        # If no solution is found (though there should be one per the problem statement)
        return []
