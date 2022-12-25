"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.



"""

from typing import List

def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    ans = []
    nums.sort()
    for i in queries:
        length = 0
        for n in nums:
            if n <= i:
                i -= n
                length += 1
        ans.append(length)
    return ans

nums, queries = [4,5,2,1], [3,10,21]
print(answerQueries(nums,queries))

"""
Time Complexity: O(N*M) even though we sorted using which is  (n log n), N*M is greater so we need to take that
Since we're going based off the length of queries and nums

Space: O(N)


"""