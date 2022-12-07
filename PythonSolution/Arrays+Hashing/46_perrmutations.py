"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
from typing import List
def permute(nums: List[int]) -> List[List[int]]:

    def permutations(arr):
        if len(arr) == 0:
            return []
        
        if len(arr) == 1:
            return [arr]
        
        possible_perms = []
        
        for a in range(len(arr)):
            #Ref first elem
            first = arr[a]
            
            #Extract the other elems
            splits = arr[:a] + arr[a+1:]
            
            for p in permutations(splits):
                possible_perms.append([first]+p)
        return possible_perms
    
    all_perms = permutations(nums)
    return all_perms

Case1 = [1,2,3]
print(permute(Case1))

"""
Time Complexity: O(N)
Space: O(N)

"""