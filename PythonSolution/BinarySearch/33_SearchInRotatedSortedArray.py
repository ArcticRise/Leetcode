"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

"""

from typing import List


def search( nums: List[int], target: int) -> int:
    left,right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        
        #Logic Needed since the array is rotated
        elif nums[mid] >= nums[left]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid -1
            else:
                left  = mid + 1
    return -1

Case1,target = [4,5,6,7,0,1,2],0
print(search(Case1,target))

"""
Time Complexity: O(Log n) -> since its binary search we're eliminating potentially half of the numbers if it doesnt fit our target
Space: O(1)

"""