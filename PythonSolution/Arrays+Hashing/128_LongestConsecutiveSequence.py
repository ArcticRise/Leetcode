"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


input: [100,4,200,1,3,2]
output: 4, LCS = 1,2,3,4

"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    ls = 0
    num_set = set(nums)
    
    for n in num_set:
        if n-1 not in num_set:
            s = 1
            while n + s in num_set:
                s += 1
            ls = max(ls,s)
    return ls

Case1 = [100,4,200,1,3,2]
print(longestConsecutive(Case1))

"""
Time Complexity: O(n)
Space: O(N)

This works because were keeping track if the start of the seq exist then checking if the next greater num exist

ex: for elem 1, 0 does not exist in the set, so s = 1 then we check the n + s if in set so 2 and so forth

"""