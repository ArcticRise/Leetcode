"""
Given an Integer array nums return True if a values appear at least twice

Ex [1,2,3,1] - > True cause 1 appears twice

"""

from typing import List

#TypeDef Coding kkkk
def checkDups(nums: List[int]) -> bool:
    #Initalize Set
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

Case1 = [1,2,3,4] #False
Case2 = [1,2,3,4,4] #True

print(checkDups(Case1))
print(checkDups(Case2))

"""
Solution runs in O(n) time complexity and O(N) space complexity

b/c loops all elems in array/list but also uses another data struct to keep track if seen
use Set b/c its fasters compared to array for lookup

"""
