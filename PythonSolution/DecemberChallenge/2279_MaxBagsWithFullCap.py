"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.


Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.

"""

from typing import List

def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    num_rocks_needed = []
    for r in range(len(rocks)):
        num_rocks_needed.append(capacity[r]-rocks[r])
    num_rocks_needed.sort()

    ans = 0
    for r in num_rocks_needed:
        if r == 0:
            ans += 1
        elif additionalRocks - r >= 0:
            ans += 1
            additionalRocks -= r
    return ans

capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2

print(maximumBags(capacity,rocks,additionalRocks))
"""
Time: O(nlogn) - > Sorting
Space: O(N)

"""