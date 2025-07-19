"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]
    # Calculate postfix products and combine with prefix products
    # For each index i, multiply its prefix product with postfix product
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result


print(productExceptSelf([1,2,4,6]))      # Should print: [48,24,12,8]
print(productExceptSelf([-1,0,1,2,3]))  # Should print: [0,-6,0,0,0]