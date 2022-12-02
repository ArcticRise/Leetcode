"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List
from collections import defaultdict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_map = defaultdict(int)
    for n in nums:
        freq_map[n] += 1
        #Mpa freq to val
    freq_map2 = [[] for i in range(len(nums)+1)]
    for x,v in freq_map.items():
        freq_map2[v].append(x)
    
    ans = []
    for i in range(len(freq_map2)-1,-1,-1):
        for j in freq_map2[i]:
            ans.append(j)
            if len(ans) == k:
                return ans
    return ans


"""
Time Complexity: O(N)
Space: O(K)

"""

Case1,k =[1,1,1,2,2,3],2
print(topKFrequent(Case1,k))