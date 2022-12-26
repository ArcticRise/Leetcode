"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


"""

from typing import List


#Going Backwards Solutioin
def canJump(nums: List[int]) -> bool:
    last = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        if i + nums[i] >= last:
            last = i
    return last == 0


#Going Forward Solution
def canJumpForward(nums: List[int]) -> bool:
    last = 0
    for i,n in enumerate(nums):
        if i > last:
            return False
        last = max(last,i+n)
    return True


nums = [2,3,1,1,4]
print(canJump(nums))
print(canJumpForward(nums))

"""

Time: O(N)
Space: O(1)

"""