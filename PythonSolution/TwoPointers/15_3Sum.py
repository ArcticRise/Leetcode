"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""


from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right] 
            if total > 0 :
                right -= 1
            elif total == 0:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            else:
                left += 1
    return res

"""
Time Complexity: O(N Log N) had to sort the array
Space: O(N)

"""