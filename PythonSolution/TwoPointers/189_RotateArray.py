"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

"""
from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    def reverse(index1,index2):
        left, right = index1, index2
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
    k %= len(nums)
    
    #rev first half
    reverse(0,len(nums)-k-1)
    #rev second half
    reverse(len(nums)-k,len(nums)-1)
    #reverse whole array
    reverse(0,len(nums)-1)


Case1, k = [1,2,3,4,5,6,7],3
rotate(Case1,k)
print(Case1)

"""
Time Complexity: O(N)
Space: O(1)

Rev first half gives 4321
Rev second half gives 765
reverse whole array which is 4321765 = 5671234
"""

