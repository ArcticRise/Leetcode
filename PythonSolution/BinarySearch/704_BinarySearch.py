"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""

from typing import List


def search( nums: List[int], target: int) -> int:
    left,right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

Case1,target = [-1,0,3,5,9,12],9
print(search(Case1,target))

"""
Time Complexity: O(Log n) -> since its binary search we're eliminating potentially half of the numbers if it doesnt fit our target
Space: O(1)

"""