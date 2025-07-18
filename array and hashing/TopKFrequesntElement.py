"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    # Create buckets where index represents frequency
    # bucket[i] contains numbers that appear i times
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        bucket[freq].append(num)
    
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        #start from the highest frequency
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
                