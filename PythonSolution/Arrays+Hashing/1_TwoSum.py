"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

from collections import defaultdict
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    #Use map keep track of index
    indices = defaultdict(int)
    for i in range(len(nums)):
        if target-nums[i] in indices:
            return [indices[target-nums[i]],i]
        indices[nums[i]] = i
    return [-1,-1]

print(twoSum([2,7,11,15],9))

"""
Time complexity: O(N)
Space Complexity: O(N)

"""

