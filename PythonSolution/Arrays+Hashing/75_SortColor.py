"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""

from typing import List

def sortColors(nums: List[int]) -> None:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0) + 1
    
    index = 0
    for i in range(3): # O(1)
        if i in freq:
            for j in range(freq[i]): 
                nums[index] = i
                index += 1

case1 = [2,0,2,1,1,0]
sortColors(case1)
print(case1)

"""
Time Complexity: O(N)
Space: O(N)

"""