"""
Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
"""

def twoSums(nums: list[int], target: int) -> list[int]:
    num_maps = {}
    for i, num in enumerate(nums):
        # calculate the diff
        diff = target - num

        if diff in num_maps:
            return [min (num_maps[diff], i), max(num_maps[diff], i)]
        num_maps[num] = i
    # if not found
    return []

print(twoSums([3,4,5,6], 7))
print(twoSums([4,5,6], 10))
print(twoSums([5,5], 10))

