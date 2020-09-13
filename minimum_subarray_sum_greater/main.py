# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous sub-array of which the sum ≥ s.
# If there isn't one, return 0 instead.

# Example:

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Explanation: the sub-array [4,3] has the minimal length under the problem constraint.

class Solution:
    def min_sub_array_len(self, nums, s):
        start = 0
        answer = 0
        while start < len(nums):
            partial_sum = 0
            i = start
            minimal_length = 0
            while partial_sum < s and i < len(nums):
                partial_sum += nums[i]
                minimal_length = minimal_length + 1
                i = i + 1
            if partial_sum >= 0 and partial_sum >= s:
                print("Sum: " + str(partial_sum) + " for elements " + str(nums[start: i]) + " no: " + str(
                    len(nums[start:i])))
                if answer == 0 or minimal_length < answer:
                    answer = minimal_length
            start = start + 1

        return answer


print("When solution found:")
print("min length " + str(Solution().min_sub_array_len([2, 3, 1, 2, 4, 3], 7)))
print()
print("When solution not found:")
print("min length " + str(Solution().min_sub_array_len([2, 3, 1, 2, 4, 3], 17)))
