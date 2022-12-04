"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

input = numbers = [2,7,11,15], target = 9
output: [1,2]


"""
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left,right = 0, len(numbers)-1
    
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left+1,right+1]
        
        #Since its sorted if we move to the right-1 the sum would dec vice versa
        elif total > target:
            right -= 1
        else:
            left += 1
    return [-1,-1]

Case1, k = [2,7,11,15], 9
print(twoSum(Case1,k))

"""
Time Complexity : O(N)
Space: O(1) -> ALways length 2

"""
