"""
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

"""

import heapq
from typing import List


def minStoneSum(piles: List[int], k: int) -> int:
    heap = []
    for i in piles:
        #In Python heap is usually min heap, but if we insert -val then that would turn 
        #the heap into a max heap
        heapq.heappush(heap,-i)
    index = 0
    while index < k:
        val = heapq.heappop(heap) * -1
        val -= val // 2
        heapq.heappush(heap,-val)
        index += 1
    
    ans = 0
    while heap:
        ans += heapq.heappop(heap) * - 1

    return ans

Case1, k  = [5,4,9],2
print(minStoneSum(Case1,k))

"""
Time Complexity: O(N + NlogN)
Space: O(N)


"""